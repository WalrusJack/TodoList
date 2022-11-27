from django.shortcuts import render, redirect
from .models import Todo
from .forms import TaskForm


# Create your views here.
def index(request):
    search_term = request.GET.get('search-term') or ''
    tasks = Todo.objects.filter(task_name__icontains=search_term)
    context = {'tasks': tasks}
    return render(request, 'index.html', context)


def add(request):
    if request.method == 'POST':
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = TaskForm()
    context = {'form': form}
    return render(request, 'add.html', context)


def update(request, task_id):
    task = Todo.objects.get(id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST or None, instance=task)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = TaskForm(instance=task)
    context = {'form': form, 'task_id': task_id}
    return render(request, 'update.html', context)


def delete(request, task_id):
    task = Todo.objects.get(id=task_id)
    task.delete()
    return redirect('index')
