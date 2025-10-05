from django.shortcuts import render, get_object_or_404, redirect
from ..models import User, Task
from ..forms import DoTasks
from django.http import HttpResponseRedirect

# |TASKS RELATED VIEWS|

# Creates a task from users input
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
 
# Deletes the specified task by the user
def delete_task(request, user_id, task_id):
    task = get_object_or_404(Task, id = task_id)
    task.delete()
    referer = request.META.get('HTTP_REFERER')
    return HttpResponseRedirect(referer)

""" 
Completes the specified task by the user from the uncompleted tasks view
Changes its state to Complete, and allows it to be visualize in the "completed tasks" view
"""
def complete_task(request, user_id, task_id):
    task = get_object_or_404(Task, id = task_id)
    task.completed = True
    task.save()
    return redirect(f'/{user_id}')

""" 
Uncompletes the specified task by the user from the completed tasks view
Changes its state to Uncomplete, and allows it to be visualize in the "uncompleted tasks" view
"""
def uncomplete_task(request, user_id, task_id):
    task = get_object_or_404(Task, id = task_id)
    task.completed = False
    task.save()
    return redirect(f'/{user_id}/completed_tasks')

""" 
Modify the specified task by the user
A task can be modifed form the uncompleted or completed tasks
It only modifies the fields with changes, is nothing is changed the task remains the same
"""
def modify_task(request, user_id, task_id, completed):
    # Completed references where the functions is called: 0 =  from uncompleted tasks, 1 = from completed tasks

    user = get_object_or_404(User, id = user_id)
    task = get_object_or_404(Task, id = task_id)
    if request.method == 'GET':
        return render(request, "modify_task.html", {
            'user': user,
            'form': DoTasks(initial={
                'name' : task.name,
                'description' : task.description,
                'deadline' : task.deadline
            })
        })
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