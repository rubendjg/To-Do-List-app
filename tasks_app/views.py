from django.shortcuts import render, get_object_or_404, redirect
from .models import User, Task
from .forms import DoTasks, DoUsers
from django.http import HttpResponseRedirect

# Create your views here.
def index(request): 
    return render(request, "index.html")

def user_tasks(request, user_id):
    user = get_object_or_404(User, id=user_id)
    tasks = user.tasks.filter(completed = False)
    tasks_list = list()

    return render(request, "user.html", {
        'user':  user,
        'tasks': tasks
    })

def completed_tasks(request, user_id):
    user = get_object_or_404(User, id=user_id)
    tasks = user.tasks.filter(completed = True)
    tasks_list = list()
    
    return render(request, "completed.html", {
        'user':  user,
        'tasks': tasks
    })
    
def create_user(request):
    if request.method == "GET":
        return render(request, "create_user.html", {
            'form': DoUsers()
        })
    else:
        User.objects.create(username = request.POST['username'], password = request.POST['password'])
        user = User.objects.get(username = request.POST['username'], password = request.POST['password'])
        return redirect(f'/{user.id}')
    
def user_login(request):
    if request.method == "GET":
        return render(request, "login.html", {
            'form': DoUsers()
        })
    else:
        user = User.objects.get(username = request.POST['username'], password = request.POST['password'])
        return redirect(f'/{user.id}')

# Creating a task from the user input
def create_task(request, user_id):
    user = get_object_or_404(User, id = user_id)
    if request.method == "GET":
        return render(request, "create_task.html", {
        'user': user,
        'form': DoTasks()
    })
    else:
        Task.objects.create(name = request.POST['name'], description = request.POST['description'], deadline = request.POST['deadline'], user = user)
        return redirect(f'/{user_id}')
 
def delete_task(request, user_id, task_id):
    task = get_object_or_404(Task, id = task_id)
    task.delete()
    referer = request.META.get('HTTP_REFERER')
    return HttpResponseRedirect(referer)

def complete_task(request, user_id, task_id):
    task = get_object_or_404(Task, id = task_id)
    task.completed = True
    task.save()
    return redirect(f'/{user_id}')

def uncomplete_task(request, user_id, task_id):
    task = get_object_or_404(Task, id = task_id)
    task.completed = False
    task.save()
    return redirect(f'/{user_id}/completed_tasks')

def modify_task(request, user_id, task_id, completed):
    # Completed refers if the user is in the completed or uncompleted tasks: 0 = uncompleted, 1 = completed

    user = get_object_or_404(User, id = user_id)
    task = get_object_or_404(Task, id = task_id)
    if request.method == 'GET':
        return render(request, "modify_task.html", {
            'user': user,
            'form': DoTasks(initial={
                'name' : task.name,
                'description' : task.description,
                'deadline' : task.deadline
            })})
    else:
        form = DoTasks(request.POST)
        if form.is_valid():
            task.name = form.cleaned_data['name']
            task.description = form.cleaned_data['description']
            task.deadline = form.cleaned_data['deadline']

            task.save()
            if (completed == 0):
                return redirect(f"/{user_id}")
            else:
                return redirect(f"/{user_id}/completed_tasks")

def return_to_users(request):
    return redirect("/")

def return_to_tasks(request, user_id):
    return redirect(f"/{user_id}")