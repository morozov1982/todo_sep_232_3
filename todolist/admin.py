from django.contrib import admin

from todolist.models import Category, TodoList

admin.site.register(Category)
admin.site.register(TodoList)
