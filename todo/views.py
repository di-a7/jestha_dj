from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Todolist
# Create your views here.
def home(request):
    return HttpResponse("Hello")

def aboutus(request):
    return HttpResponse("This is aboutus page.")

# aboutus, contact

def index(request):
    people = [
    {
        "name": "Ram Bahadur",
        "age": 28,
        "gender": "Male",
    },
    {
        "name": "Sita Sharma",
        "age": 50,
        "gender": "Female",
    },
    {
        "name": "Hari Prasad",
        "age": 2,
        "gender": "Male",
    },
    {
        "name": "Gita Koirala",
        "age": 30,
        "gender": "Female",
    },
    {
        "name": "Gita Koirala",
        "age": 50,
        "gender": "Female",
    },
    {
        "name": "Gita Koirala",
        "age": 10,
        "gender": "Female",
    }
]

    context = {
        "header":"Index Page",
        "para":"This is a index page.",
        "people": people
    }
    return render(request, 'index.html', context)

def contact(request):
    return render(request,'contact.html')


def todolist(request):
    tasks = Todolist.objects.all()
    
    context = {
        "tasks":tasks
    }
    return render(request, 'task.html', context)

def task_create(request):
    if request.method == "POST":
        title_input = request.POST.get('title')
        description_input = request.POST.get('description')
        
        if title_input == '' or description_input == '':
            context = {
                "error":"Both title and description are required."
            }
            return render(request, 'create.html', context)
        else:
            Todolist.objects.create(title = title_input, description = description_input)
            return redirect('/todolist/')
    return render(request, 'create.html')

def mark_complete(request, id):
    task = Todolist.objects.get(id = id)
    task.status = True
    task.save()
    return redirect('/todolist/')

def edit(request, id):
    task = Todolist.objects.get(id = id)
    context = {
        "tasks" : task
    }
    if request.method == "POST":
        title_update = request.POST.get('title')
        description_update = request.POST.get('description')
        
        task.title = title_update
        task.description = description_update
        task.save()
        return redirect('/todolist/')
    return render(request,'edit.html', context)

def delete(request, id):
    task = Todolist.objects.get(id = id)
    task.delete()
    return redirect('/todolist/')
