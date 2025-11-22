from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from ..models import User

# |WELCOME PAGE RELATED VIEWS|
def index(request): 
    return render(request, "index.html")

# Returns to the home page
def return_to_users(request):
    users_url = reverse('index')
    return redirect(users_url)


# |MAIN PAGE VIEWS| 
# Shows the tasks associated to the specified user
def user_tasks(request, user_id, completed=False):
    if request.session.get('user_id') != user_id:
        return redirect('index')
    
    user = get_object_or_404(User, id=user_id)
    tasks = user.tasks.filter(completed=completed)

    template = "completed.html" if completed else "user.html"

    next_url = request.path  

    return render(request, template, {
        'user': user,
        'tasks': tasks,
        'next': next_url
    })


# Returns to the users tasks
def return_to_tasks(request, user_id):
    if request.session.get('user_id') != user_id:
        return redirect('index')

    user_page_url = reverse('main', args=[user_id])
    return redirect(user_page_url)
