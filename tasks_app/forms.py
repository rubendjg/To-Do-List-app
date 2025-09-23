from django import forms

class DoTasks(forms.Form):
    name = forms.CharField(label = "Task's name", max_length = 100)
    description = forms.CharField(label = "Task's description", max_length = 100, required = False)
    deadline = forms.DateField(label = "Deadline", widget=forms.DateInput(attrs={'type': 'date'})) #, required = False)
    

class DoUsers(forms.Form):
    username = forms.CharField(label = "Username", max_length = 25)
    password = forms.CharField(label = "Password", max_length = 40, widget = forms.PasswordInput)

