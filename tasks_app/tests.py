from django.test import TestCase
from .models import *
from .forms import DoTasks, DoUsers, ModifyUsers
from datetime import date, timedelta
from django.urls import reverse

# Create your tests here.

class UserTestCase(TestCase):

    def setUp(self):
        self.user = User(username = "Lucrecia")
        self.user.set_password("test")
        self.user.save()

        session = self.client.session
        session['user_id'] = self.user.id
        session.save()


    def test_create_user(self):
        self.assertTrue(User.objects.filter(id = self.user.id).exists())
    
    def test_change_username(self):
        user = self.user

        # Modify username
        user.set_username("Felipe")
        user.save() 

        # Fetch user from database
        updated_user = User.objects.get(id = user.id)
        self.assertEqual(updated_user.get_username(), "Felipe")

    def test_change_password(self):
        user = self.user

        # Modify username
        user.set_password("modified")
        user.save() 

        # Fetch user from database
        updated_user = User.objects.get(id = user.id)
        self.assertTrue(updated_user.check_password("modified"))
        self.assertFalse(updated_user.check_password("test"))
    
    def test_delete_user(self):
        user = self.user

        # Delete User
        user.delete()
        self.assertFalse(User.objects.filter(id = user.id).exists())

class TasksTestCase(TestCase):
    
    def setUp(self):
        self.user = User(username = "Ashe")
        self.user.set_password("test")
        self.user.save()

        session = self.client.session
        session['user_id'] = self.user.id
        session.save()

        self.task = Task(
            name = "Test Task",
            description = "This is a test task",
            deadline = date.today(),
            user = self.user
        )
        self.task.save()

    def test_task_creation(self):
        self.assertTrue(Task.objects.filter(id = self.task.id).exists())

    def test_task_modify_name(self):
        task = self.task
        task.name = "New name"
        task.save()

        updated_task = Task.objects.get(id = task.id)
        self.assertEqual(updated_task.name, "New name")
        
    def test_task_modify_description(self):
        task = self.task
        task.description = "New description"
        task.save()

        updated_task = Task.objects.get(id = task.id)
        self.assertEqual(updated_task.description, "New description")
    
    def test_task_modify_deadline(self):
        task = self.task
        task.deadline = date.today() + timedelta(days=3)
        task.save()

        updated_task = Task.objects.get(id = task.id)
        self.assertEqual(updated_task.deadline, date.today() + timedelta(days=3))
    
    def test_task_complete(self):
        task = self.task
        task.completed = True
        task.save()

        updated_task = Task.objects.get(id = task.id)
        self.assertEqual(updated_task.completed, True)

    def test_task_uncomplete(self):
        task = self.task
        task.completed = False
        task.save()

        updated_task = Task.objects.get(id = task.id)
        self.assertEqual(updated_task.completed, False)

class GeneralViewsTestCase(TestCase):
    
    def setUp(self):
        self.user = User(username = "Kelsier")
        self.user.set_password("test")
        self.user.save()

        session = self.client.session
        session['user_id'] = self.user.id
        session.save()

        self.t1 = Task.objects.create(name="Uncompleted Task", description="", deadline="2025-01-01", user=self.user)
        self.t2 = Task.objects.create(name="Completed Task", description="", deadline="2025-01-01", completed=True, user=self.user)

    def test_show_uncompleted_tasks(self):
        url = reverse('main', args = [self.user.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user.html')

        tasks = response.context['tasks']
        self.assertIn(self.t1, tasks)
        self.assertNotIn(self.t2, tasks)

    def test_show_completed_tasks(self):
        url = reverse('completed_tasks', args = [self.user.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'completed.html')

        tasks = response.context['tasks']
        self.assertIn(self.t2, tasks)
        self.assertNotIn(self.t1, tasks)

    def test_return_to_tasks(self):
        url = reverse('return_to_tasks', args = [self.user.id])
        response = self.client.get(url)
        self.assertRedirects(response, reverse('main', args = [self.user.id]))

class TasksViewsTestCase(TestCase):
    def setUp(self):
        self.user = User(username = "Hornet")
        self.user.set_password("test")
        self.user.save()

        session = self.client.session
        session['user_id'] = self.user.id
        session.save()

        self.uncompleted_task = Task.objects.create(name = "Task", description = "", deadline = "2025-01-01", user=self.user)
        self.completed_task = Task.objects.create(name="Task", description = "", deadline = "2025-01-01", completed = True, user = self.user)
    
    def test_create_task_get(self):
        url = reverse('create_task', args = [self.user.id])

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_task.html')
        # Check if user in the response is the same as the user sent
        self.assertEqual(response.context['user'], self.user) 
        self.assertIn('form', response.context)
        self.assertIsInstance(response.context['form'], DoTasks)

    def test_create_task_post(self):
        url = reverse('create_task', args = [self.user.id])

        data = {
            'name': "New Task",
            'description': '',
            'deadline': "2025-12-15"
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('main', args = [self.user.id]))
    
    def test_delete_uncompleted_task(self):
        url = reverse('delete_task', args = [self.user.id, self.uncompleted_task.id])
        response = self.client.post(url)

        self.assertRedirects(response, reverse('main', args = [self.user.id]))
        self.assertFalse(Task.objects.filter(id = self.uncompleted_task.id).exists())

    def test_delete_completed_task(self):
        next_url = reverse('completed_tasks', args=[self.user.id])
        url = reverse('delete_task', args = [self.user.id, self.completed_task.id]) + f'?next={next_url}'
        
        response = self.client.post(url)

        self.assertRedirects(response, reverse('completed_tasks', args = [self.user.id]))
        self.assertFalse(Task.objects.filter(id = self.completed_task.id).exists())

    def test_complete_task(self):
        url = reverse('modify_completition_task', args = [self.user.id, self.uncompleted_task.id])
        response = self.client.post(url)

        self.assertRedirects(response, reverse('main', args = [self.user.id]))
        self.assertTrue(Task.objects.filter(id = self.uncompleted_task.id).get().completed)

    def test_uncomplete_task(self):
        next_url = reverse('completed_tasks', args=[self.user.id])
        url = reverse('modify_completition_task', args = [self.user.id, self.completed_task.id]) + f'?next={next_url}'

        response = self.client.post(url)

        self.assertRedirects(response, reverse('completed_tasks', args = [self.user.id]))
        self.assertFalse(Task.objects.filter(id = self.completed_task.id).get().completed)

    # The tests for modifying a task will only cover the modification of uncompleted tasks, as we checked that the method for checking from where the user calls the function works

    def test_modify_task_get(self):
        url = reverse('modify_task', args = [self.user.id, self.uncompleted_task.id])

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'modify_task.html')

        self.assertEqual(response.context['user'], self.user) 
        self.assertIn('form', response.context)
        self.assertIsInstance(response.context['form'], DoTasks)

        self.assertEqual(response.context['form']['name'].value(), self.uncompleted_task.name)
        self.assertEqual(response.context['form']['description'].value(), self.uncompleted_task.description)
        self.assertEqual(response.context['form']['deadline'].value().strftime("%Y-%m-%d"), self.uncompleted_task.deadline)

    # This are all Post test for modifying a task
    def test_modify_task_name(self):
        url = reverse('modify_task', args = [self.user.id, self.uncompleted_task.id])

        response = self.client.post(url, {
            'name': "New Name",
            'description': self.uncompleted_task.description,
            'deadline': self.uncompleted_task.deadline
        } )

        updated_task = Task.objects.get(id=self.uncompleted_task.id)

        self.assertEqual(updated_task.name, "New Name")

        self.assertEqual(updated_task.description, self.uncompleted_task.description)
        self.assertEqual(updated_task.deadline.strftime("%Y-%m-%d"), self.uncompleted_task.deadline)
    
    def test_modify_task_description(self):
        url = reverse('modify_task', args = [self.user.id, self.uncompleted_task.id])

        response = self.client.post(url, {
            'name': self.uncompleted_task.name,
            'description': "New Description",
            'deadline': self.uncompleted_task.deadline
        } )

        updated_task = Task.objects.get(id=self.uncompleted_task.id)

        self.assertEqual(updated_task.description, "New Description")

        self.assertEqual(updated_task.name, self.uncompleted_task.name)
        self.assertEqual(updated_task.deadline.strftime("%Y-%m-%d"), self.uncompleted_task.deadline)
    
    def test_modify_task_description(self):
        url = reverse('modify_task', args = [self.user.id, self.uncompleted_task.id])

        response = self.client.post(url, {
            'name': self.uncompleted_task.name,
            'description': self.uncompleted_task.description,
            'deadline': "2026-01-10"
        } )

        updated_task = Task.objects.get(id=self.uncompleted_task.id)

        self.assertEqual(updated_task.deadline.strftime("%Y-%m-%d"), "2026-01-10")

        self.assertEqual(updated_task.name, self.uncompleted_task.name)
        self.assertEqual(updated_task.description, self.uncompleted_task.description)


class UserViewsTestCase(TestCase):
    def setUp(self):
        self.user = User(username = "Kelsier")
        self.raw_password = "test"
        self.user.set_password(self.raw_password)
        self.user.save()

        session = self.client.session
        session['user_id'] = self.user.id
        session.save()

    # User Login Tests
    def test_user_login_get(self):
        url = reverse('login')

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

        self.assertIn('form', response.context)
        self.assertIsInstance(response.context['form'], DoUsers)

    def test_user_login_post_success(self):
        url = reverse('login') 
        response = self.client.post(url, {
            'username': self.user.username,
            'password': self.raw_password
        })

        self.assertRedirects(response, reverse('main', args = [self.user.id]))
    
    def test_user_login_post_wrong_username(self):
        url = reverse('login') 
        response = self.client.post(url, {
            'username': 'Wrong Username',
            'password': self.raw_password
        })

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login') + '?error=1')

    def test_user_login_post_wrong_password(self):
        url = reverse('login') 
        response = self.client.post(url, {
            'username': self.user.username,
            'password': "Wrong password"
        })

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login') + '?error=1')

    # Create User Tests
    def test_create_user_get(self):
        url = reverse('new_user')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "create_user.html")

        self.assertIn('form', response.context)
        self.assertIsInstance(response.context['form'], DoUsers)

    def test_create_user_success_post(self):
        url = reverse('new_user')
        response = self.client.post(url, {
            'username': "Elizabeth",
            'password': "test_password"
        })

        self.assertTrue(User.objects.filter(username="Elizabeth").exists())

        user = User.objects.get(username="Elizabeth")
        self.assertRedirects(response, reverse('main', args = [user.id]))

    def test_create_existing_user_post(self):
        url = reverse('new_user')
        response = self.client.post(url, {
            'username': "Kelsier",
            'password': "test_password"
        })  

        self.assertRedirects(response, reverse('new_user') + '?error=1')

    def test_create_user_wrong_format_post(self):
        url = reverse('new_user')
        response = self.client.post(url, {
            'username': "Booker"
        }) 
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "create_user.html")
        
        self.assertFalse(User.objects.filter(username="Booker").exists())
    
    # Modify User Tests
    def test_modify_user_get(self):
        url = reverse('modify_user', args = [self.user.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'modify_user.html')

        self.assertIsInstance(response.context['form'], ModifyUsers)
        self.assertEqual(response.context['user'], self.user)
    
    def test_modify_user_change_username_post(self):
        url = reverse('modify_user', args=[self.user.id])
        new_username = "NewUsername"

        response = self.client.post(url, data={
            'username': new_username,
            'password': ''
        })

        self.user.refresh_from_db()
        self.assertEqual(self.user.username, new_username)
        self.assertRedirects(response, reverse('main', args=[self.user.id]))

    def test_modify_user_post_change_password_post(self):
        url = reverse('modify_user', args=[self.user.id])
        new_password = "newpassword"

        response = self.client.post(url, data={
            'username': self.user.username,
            'password': new_password
        })

        self.user.refresh_from_db()
        self.assertTrue(self.user.check_password(new_password))
        self.assertRedirects(response, reverse('main', args=[self.user.id]))

    def test_modify_user_username_conflict_post(self):
        url = reverse('modify_user', args=[self.user.id])
        other_user = User(username="OtherUser")
        other_user.set_password("otherpass")
        other_user.save()

        response = self.client.post(url, data={
            'username': other_user.username,
            'password': ''
        })

        self.user.refresh_from_db()
        self.assertEqual(self.user.username, "Kelsier")
        self.assertRedirects(response, reverse('modify_user', args=[self.user.id]) + '?error=2')

    # Delete User Tests
    def test_delete_user_success(self):
        url = reverse('delete_user', args = [self.user.id])
        response = self.client.post(url, {
            'password': self.raw_password
        })

        self.assertRedirects(response, reverse('index'))
        self.assertFalse(User.objects.filter(id = self.user.id).exists())

    def test_delete_user_wrong_password(self):
        url = reverse('delete_user', args = [self.user.id])
        response = self.client.post(url, {
            'password': "Wrong password"
        })

        self.assertRedirects(response, reverse('modify_user', args = [self.user.id]) + '?error=1')
        self.assertTrue(User.objects.filter(id = self.user.id).exists())
    
    def test_delete_user_get(self):
        url = reverse('delete_user', args = [self.user.id])
        response = self.client.get(url)

        self.assertRedirects(response, reverse('modify_user', args = [self.user.id]) )
