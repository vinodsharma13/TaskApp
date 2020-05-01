from django.urls import path
from taskApp import views
urlpatterns = [
    path('', views.todolist, name='todolist'),
    path('delete/<id>', views.delete_task, name='delete_task'),
    path('edit/<id>', views.edit_task, name='edit_task'),
    path('complete/<id>', views.complete_task, name='complete_task'),
    path('pending/<id>', views.pending_task, name='pending_task'),
   
    

]
