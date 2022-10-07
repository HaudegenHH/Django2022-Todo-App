from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

from .models import Task

# inherits form the ListView
# view looks for a template which is prefixed with 'task' and ends with '_list.html'
class TaskList(ListView):  
  model = Task
  context_object_name = 'tasks'

# looks for 'task_detail.html' by default
# if you want it to look for a different tmplate set template_name
class TaskDetail(DetailView):
  model = Task
  context_object_name = 'task'
  template_name = 'base/task.html'

# looks by default for 'task_form.html'
class TaskCreate(CreateView):
  model = Task
  fields = '__all__'
  success_url = reverse_lazy('tasks')


class TaskUpdate(UpdateView):
  model = Task
  fields = '__all__'
  success_url = reverse_lazy('tasks')


# by default looks for "<modelname>_confirm_delete.html"
class TaskDelete(DeleteView):
  model = Task
  context_object_name = 'task'
  success_url = reverse_lazy('tasks')

