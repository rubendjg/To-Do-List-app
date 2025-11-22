from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from ..models import User, Task
from ..forms import DoTasks
from django.http import HttpResponseRedirect

# |TASKS RELATED VIEWS|

# Creates a task from users input 
def create_task(request, user_id):
    if request.session.get('user_id') != user_id:
        return redirect('index')
    
    user = get_object_or_404(User, id=user_id)

    if request.method == "GET":
        return render(request, "create_task.html", {
            'user': user,
            'form': DoTasks()
        })

    Task.objects.create(
        name=request.POST['name'],
        description=request.POST['description'],
        deadline=request.POST['deadline'],
        user=user
    )

    return redirect(reverse('main', args=[user_id]))
 
# Deletes the specified task by the user
def delete_task(request, user_id, task_id):
    if request.session.get('user_id') != user_id:
        return redirect('index')
    
    task = get_object_or_404(Task, id=task_id)
    task.delete()

    next_url = request.GET.get("next") or reverse("main", args=[user_id])
    return redirect(next_url)
    

""" 
Completes the specified task by the user from the uncompleted tasks view
Changes its state to Complete, and allows it to be visualize in the "completed tasks" view
"""
def modify_completition_state_task(request, user_id, task_id):
    if request.session.get('user_id') != user_id:
        return redirect('index')

    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save()

    next_url = request.GET.get("next") or reverse("main", args=[user_id])
    return redirect(next_url)

""" 
Modify the specified task by the user
A task can be modifed form the uncompleted or completed tasks
It only modifies the fields with changes, if nothing is changed the task remains the same
"""
def modify_task(request, user_id, task_id):
    if request.session.get('user_id') != user_id:
        return redirect('index')
    
    user = get_object_or_404(User, id=user_id)
    task = get_object_or_404(Task, id=task_id)

    next_url = request.GET.get("next") or request.POST.get("next") or reverse("main", args=[user_id])

    if request.method == 'GET':
        return render(request, "modify_task.html", {
            'user': user,
            'form': DoTasks(initial={
                'name': task.name,
                'description': task.description,
                'deadline': task.deadline
            }),
            'next': next_url
        })

    form = DoTasks(request.POST)
    if form.is_valid():
        task.name = form.cleaned_data['name']
        task.description = form.cleaned_data['description']
        task.deadline = form.cleaned_data['deadline']
        task.save()
        return redirect(next_url)

    return render(request, "modify_task.html", {
        'user': user,
        'form': form,
        'next': next_url
    })
