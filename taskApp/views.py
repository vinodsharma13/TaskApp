from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import TaskList
from taskApp.forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def todolist(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        try:
            if form.is_valid():
                instance = form.save(commit=False)
                instance.manage  = request.user
                instance.save()
            messages.success(request,("New Task Added!"))
            return redirect('todolist')
        except:
            pass
    else : 
        all_tasks = TaskList.objects.filter(manage=request.user)
        paginator = Paginator(all_tasks,5)
        page = request.GET.get('pg')
        all_tasks = paginator.get_page(page)
        return render(request, 'todolist.html', {'all_tasks': all_tasks})

def index(request):
    context = {
        'index_text': "Welcome Home Adimy."
    }
    return render (request, 'index.html', context)

def about(request):
    context = {
        'welcome_text': "Welcome About page."
    }
    return render (request, 'about.html', context)

def contact(request):
    context = {
        'welcome_text': "Welcome Contact page."
    }
    return render (request, 'contact.html', context)

@login_required
def delete_task(request,id):
    task = TaskList.objects.get(pk=id)
    if task.manage == request.user:
        task.delete()
        return redirect('todolist')
    else :
        messages.success(request,("Access Restricted, you are not allowed!"))

@login_required
def edit_task(request,id):
    if request.method == "POST":
        task_obj = TaskList.objects.get(pk=id)
        form = TaskForm(request.POST or None, instance = task_obj )
        try:
            if form.is_valid():
                form.save()
            messages.success(request,("Task edited!"))
            return redirect('todolist')
        except:
            pass
    else : 
        task_obj = TaskList.objects.get(pk=id)
        return render(request, 'edit.html', {'task_obj': task_obj})

@login_required
def complete_task(request,id):
    task = TaskList.objects.get(pk=id)
    if task.manage == request.user:
        task.done = True
        task.save()
    else :
        messages.success(request,("Access Restricted, you are not allowed!"))
    return redirect('todolist')

@login_required    
def pending_task(request,id):
    task = TaskList.objects.get(pk=id)
    if task.manage == request.user:
        task.done=False
        task.save()
        return redirect('todolist')
    else:
        messages.success(request,("Access Restricted, you are not allowed!"))
        