from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    # path('<int:user_id>', views.user_tasks)
    path('<int:user_id>', views.user_tasks, name = 'main'),
    path('<int:user_id>/create', views.create_task, name = 'create_task'),
    path('create_user', views.create_user, name = 'new_user'),
    path('login', views.user_login, name = "login"),
    path('<int:user_id>/completed_tasks', views.completed_tasks, name = "completed_tasks"),
    path('<int:user_id>/<int:task_id>/delete_task', views.delete_task, name = "delete_task"),
    path('<int:user_id>/<int:task_id>/complete_task', views.complete_task, name = "complete_task"),
    path('<int:user_id>/<int:task_id>/<int:completed>/modify_task', views.modify_task, name = "modify_task"),
    path('<int:user_id>/<int:task_id>/uncomplete_task', views.uncomplete_task, name = "uncomplete_task"),
    path('return_homepage', views.return_to_users, name = "return_homepage"),
    path('<int:user_id>/return_to_tasks', views.return_to_tasks, name = "return_to_tasks"),
]   