from django.shortcuts import render
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