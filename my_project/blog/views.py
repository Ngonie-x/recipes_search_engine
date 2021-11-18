from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("This is the first URL")

def specific(request):
    return HttpResponse("This is the second URL")

def article(request, article_id):
    return render(request, 'blog/index.html')