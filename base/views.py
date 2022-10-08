from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView

# with that mixin its possible to manage roles later on 
# To restrict the access to a page, just put the mixin as a first parameter 
# to a view (decorators or middleware could be used as well for that of 
# course) which redirects to the LOGIN_URL which is defined in setting.py (at
# the bottom of the file)
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Task


class CustomLoginView(LoginView):
  template_name = 'base/login.html'
  fields = '__all__'
  redirect_authenticated_user = True

  def get_success_url(self):
    return reverse_lazy('tasks')

# inherits form the ListView
# view looks for a template which is prefixed with 'task' and ends with '_list.html'
class TaskList(LoginRequiredMixin, ListView):  
  model = Task
  context_object_name = 'tasks'

# looks for 'task_detail.html' by default
# if you want it to look for a different tmplate set template_name
class TaskDetail(LoginRequiredMixin, DetailView):
  model = Task
  context_object_name = 'task'
  template_name = 'base/task.html'

# looks by default for 'task_form.html'
class TaskCreate(LoginRequiredMixin, CreateView):
  model = Task
  fields = '__all__'
  success_url = reverse_lazy('tasks')


class TaskUpdate(LoginRequiredMixin, UpdateView):
  model = Task
  fields = '__all__'
  success_url = reverse_lazy('tasks')


# by default looks for "<modelname>_confirm_delete.html"
class TaskDelete(LoginRequiredMixin, DeleteView):
  model = Task
  context_object_name = 'task'
  success_url = reverse_lazy('tasks')

