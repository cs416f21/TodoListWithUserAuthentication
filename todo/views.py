from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
from django.contrib.auth.decorators import login_required


# @login_required decorator allows to limit access to the index page and check whether the user is authenticated
# if so, index page is rendered. If not, the user is redirected to the login page via login_url
@login_required(login_url='login')
def index(request):
    # Query the to-do table and get the todos specific for the user
    tasks = Todo.objects.filter(user=request.user)
    context = {'tasks': tasks}
    return render(request, 'todo/index.html', context)


@login_required(login_url='login')
def create_todo(request):
    form = TodoForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            # Assign the current user as the user (i.e., owner) for each task
            form.instance.user = request.user
            form.save()
            return redirect('index')

    context = {'form': form}
    return render(request, 'todo/add.html', context)


@login_required(login_url='login')
def search_todo(request):
    search_term = request.GET.get('search-term') or ''
    # query the database to find records that match with two criteria: user (user_id), and contains the search term
    tasks = Todo.objects.filter(user=request.user, task__icontains=search_term)
    context = {'tasks': tasks, 'search_term': search_term}
    return render(request, 'todo/index.html', context)


@login_required(login_url='login')
def delete_todo(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('index')





