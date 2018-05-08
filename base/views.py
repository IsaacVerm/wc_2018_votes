from django.shortcuts import render
from django.http import HttpResponse # temp for placeholders

def options(request):
    return render(request, 'base/options.html')
    
def about(request):
    return render(request, 'base/about.html')