from django.urls import path
from .views import views

urlpatterns = [
    # Welcome page related URLs
    path('', views.index, name = 'index'),
    path('return_homepage', views.return_to_users, name = "return_homepage"),

    # User related URLs
    path('login', views.user_login, name = 'login'),
    path('create_user', views.create_user, name = 'new_user'),
    path('<int:user_id>/modify_user', views.modify_user, name = 'modify_user'),
    path('<int:user_id>/delete_user', views.delete_user, name = 'delete_user'),

    # Main page related URLs
    path('<int:user_id>', views.user_tasks, name = 'main'),
    path('<int:user_id>/return_to_tasks', views.return_to_tasks, name = 'return_to_tasks'),
    path('<int:user_id>/completed_tasks', views.user_tasks, {'completed': True}, name = 'completed_tasks'),

    # Tasks related URLs
    path('<int:user_id>/create', views.create_task, name = 'create_task'),
    path('<int:user_id>/<int:task_id>/delete_task', views.delete_task, name = 'delete_task'),
    path('<int:user_id>/<int:task_id>/modify_completition_task', views.modify_completition_state_task, name = 'modify_completition_task'),
    path('<int:user_id>/<int:task_id>/modify_task', views.modify_task, name = 'modify_task'),
    
]   