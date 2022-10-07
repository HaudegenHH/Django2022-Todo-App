from django.urls import path
from . import views
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete

urlpatterns = [
  # as_view()  detects which method it is (get, post, put/patch, delete,..)
  path('', TaskList.as_view(), name='tasks'),
  # int:pk (the primary key as integer, in this case the task' id) & dont forget trailing slash!
  path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
  path('task-create/', TaskCreate.as_view(), name='task-create'),
  path('task-update/<int:pk>', TaskUpdate.as_view(), name='task-update'),
  path('task-delete/<int:pk>', TaskDelete.as_view(), name='task-delete'),
]