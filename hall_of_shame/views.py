from django.shortcuts import render
from .models import User
from django.http import HttpResponseRedirect, HttpResponse # temp for placeholders

def options(request):
    return render(request, 'hall_of_shame/options.html')
    
def debtors(request):
    debtors = User.objects.filter(paid = False)
    context = {'debtors': debtors}
    
    return render(request, 'hall_of_shame/debtors.html', context)
    
def cheaters(request):
    cheaters = User.objects.filter(times_cheated__gt = 0)
    context = {'cheaters': cheaters}
    
    return render(request, 'hall_of_shame/cheaters.html', context)