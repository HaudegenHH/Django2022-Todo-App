from django.contrib import admin
from .models import Task

# register model with admin panel
admin.site.register(Task)


