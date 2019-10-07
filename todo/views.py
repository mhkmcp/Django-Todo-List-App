from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET, require_POST
from . models import Todo
from . forms import TodoForm, NewTodoForm


def index(request):
    todo_list = Todo.objects.order_by('id')
    form = TodoForm()
    new_todo_form = NewTodoForm()
    context = {'todo_list': todo_list, 'form': new_todo_form}

    return render(request, 'todo/index.html', context)


@require_POST
def add_todo(request):
    # todo_10 = Todo.objects.get(pk=10)
    # form = TodoForm(request.POST)
    # new_form = NewTodoForm(request.POST, instance=todo_10)
    new_form = NewTodoForm(request.POST)

    if new_form.is_valid():
        # new_todo = Todo(text=form.cleaned_data['text'])
        # new_todo.save()
        new_todo = new_form.save()

    return redirect('index')


def complete_todo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()

    return redirect('index')


def delete_completed(request):
    Todo.objects.filter(complete__exact=True).delete()

    return redirect('index')


def delete_all(request):
    Todo.objects.all().delete()

    return redirect('index')