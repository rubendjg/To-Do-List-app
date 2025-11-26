from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from ..models import User
from ..forms import DoUsers, ModifyUsers

# |USER RELATED VIEWS|

# Verifies the users credentials and, if they are correct, the user access user space
def user_login(request):
    if request.method == "GET":
        return render(request, "login.html", {
            'form': DoUsers()
        })
    form = DoUsers(request.POST)
    if form.is_valid():
        username = form.cleaned_data["username"]
        raw_password = form.cleaned_data["password"]
        user = User.objects.filter(username=username).first()
        
        if user and user.check_password(raw_password):
            request.session['user_id'] = user.id
            user_url = reverse('main', args=[user.id])
            return redirect(user_url)
        else:
            login_url = reverse('login')
            return redirect(login_url + '?error=1')


    return render(request, "login.html", {"form":form})
    
"""
Creates a user, ensuring that the username is unique
Right after creation, the user accesses its user space to start using the app
"""
def create_user(request):
    if request.method == "GET":
        return render(request, "create_user.html", {
            'form': DoUsers()
        })
    
    form = DoUsers(request.POST)
    if form.is_valid():
        username = form.cleaned_data["username"]
        if User.objects.filter(username = username).exists():
            signup_url = reverse('new_user')
            return redirect(signup_url + '?error=1')
        raw_password = form.cleaned_data["password"]

        user = User(username = username)
        user.set_password(raw_password)
        user.save()
        request.session['user_id'] = user.id
        user_url = reverse('main', args=[user.id])
        return redirect(user_url)
    
    return render(request, "create_user.html", {'form': form})

"""
Modifies user information, if a field is not modified it will remain the same
Can modify both password and username
"""   
def modify_user(request, user_id, completed = False):
    if request.session.get('user_id') != user_id:
        return redirect('index')
    
    user = get_object_or_404(User, id = user_id)

    if request.method == 'GET':
        return render(request, 'modify_user.html', {
            'user': user,
            'form' : ModifyUsers(initial ={
                'username' : user.username,
                'password' : '',
            })
        })
    
    form = ModifyUsers(request.POST)
    if form.is_valid():
        new_username = form.cleaned_data['username']

        if User.objects.filter(username = new_username).exclude(id=user.id).exists():
            modify_user_url = reverse('modify_user', args=[user_id]) 
            return redirect(modify_user_url + '?error=2')

        user.set_username(new_username)    
        new_password = form.cleaned_data["password"]
        if new_password:
            user.set_password(form.cleaned_data["password"])
        user.save()

        if completed:
            return redirect(reverse('completed_tasks', args = [user_id]))
        else:
            return redirect(reverse('main', args = [user_id]))
    else:
        return render(request, 'modify_user.html', {"form":form})

# It deletes the respective user from the database
def delete_user(request, user_id):
    if request.session.get('user_id') != user_id:
        return redirect('index')
    
    user = get_object_or_404(User, id = user_id)
   
    if request.method == "POST":
        user_password = request.POST.get("password")
        if user.check_password(user_password):
            user.delete()
            main_url = reverse('index')
            return redirect(main_url)
        else:
            modify_user_url = reverse('modify_user', args=[user_id]) 
            return redirect(modify_user_url + '?error=1')
    
    return redirect('modify_user', user_id=user_id)
    
