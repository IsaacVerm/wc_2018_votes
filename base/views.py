from django.shortcuts import render
from django.http import HttpResponse # temp for placeholders

def homepage(request):
    return render(request, 'base/homepage.html')
    
def about(request):
    return render(request, 'base/about.html')