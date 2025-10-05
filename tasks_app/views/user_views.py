from django.shortcuts import render, get_object_or_404, redirect
from ..models import User
from ..forms import DoUsers

# |USER RELATED VIEWS|

# Verifies the users credentials and, if they are correct, the user access user space
def user_login(request):
    if request.method == "GET":
        return render(request, "login.html", {
            'form': DoUsers()
        })
    else:
        user = User.objects.get(username = request.POST['username'], password = request.POST['password'])
        return redirect(f'/{user.id}')

"""
Creates a user, ensuring that the username is unique
Right after creation, the user accesses its user space to start using the
"""
def create_user(request):
    if request.method == "GET":
        return render(request, "create_user.html", {
            'form': DoUsers()
        })
    else:
        User.objects.create(username = request.POST['username'], password = request.POST['password'])
        user = User.objects.get(username = request.POST['username'], password = request.POST['password'])
        return redirect(f'/{user.id}')

"""
Modifies user information, if a field is not modified it will remain the same
Can modify both password and username
"""   
def modify_user(request, user_id, completed):
    # Completed references where the functions is called: 0 =  from uncompleted tasks, 1 = from completed tasks
    user = get_object_or_404(User, id = user_id)
    if request.method == 'GET':
        return render(request, 'modify_user.html', {
            'form' : DoUsers(initial ={
                'username' : user.username,
                'password' : user.password
            })
        })
    
    else:
        form = DoUsers(request.POST)
        if form.is_valid():
            user.username = form.cleaned_data['username']
            user.password = form.cleaned_data['password']

            user.save()
            if completed == 0:
                return redirect(f'/{user_id}')
            else:
                return redirect(f'/{user_id}/completed_tasks')

# It deletes the respective user from the database
def delete_user(request, user_id, user_password):
    user = get_object_or_404(User, id = user_id)
    if user_password == user.password:
        user.delete()
        return redirect("/")
    return 