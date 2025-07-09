from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
   return HttpResponse("Hello")

def aboutus(request):
   return HttpResponse("This is aboutus page.")

# aboutus, contact

def index(request):
   context = {
      "header":"Index Page",
      "para":"This is a index page."
   }
   return render(request, 'index.html', context)