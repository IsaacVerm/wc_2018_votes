from django.shortcuts import render

def options(request):
    return render(request, 'options.html')