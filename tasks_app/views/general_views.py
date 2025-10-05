from django.shortcuts import render, get_object_or_404, redirect
from ..models import User

# |WELCOME PAGE RELATED VIEWS|
def index(request): 
    return render(request, "index.html")

# Returns to the home page
def return_to_users(request):
    return redirect("/")


# |MAIN PAGE VIEWS| 
# Shows the unfinished tasks associated to the specified user
def user_tasks(request, user_id):
    user = get_object_or_404(User, id=user_id)
    tasks = user.tasks.filter(completed = False)
    tasks_list = list()

    return render(request, "user.html", {
        'user':  user,
        'tasks': tasks
    })

# Returns to the users tasks
def return_to_tasks(request, user_id):
    return redirect(f"/{user_id}")

# Shows the completed tasks associated to the specified user
def completed_tasks(request, user_id):
    user = get_object_or_404(User, id=user_id)
    tasks = user.tasks.filter(completed = True)
    tasks_list = list()
    
    return render(request, "completed.html", {
        'user':  user,
        'tasks': tasks
    })