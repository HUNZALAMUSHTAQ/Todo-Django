
from django.forms import ModelForm, fields
from .models import Task

class TaskForm(ModelForm):
    class Meta : 
        model = Task 
        fields = '__all__'