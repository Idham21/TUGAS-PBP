from django.forms import ModelForm

from todolist.models import Task
class TaskForm(ModelForm) :
    class Meta :
        model = Task
        fields = "__all__"