from django.shortcuts import render
from .models import User
from django.http import HttpResponseRedirect, HttpResponse # temp for placeholders

def options(request):
    return render(request, 'hall_of_shame/options.html')
    
def debtors(request):
    debtors = User.objects.filter(paid = False)
    context = {'debtors': debtors}
    
    return render(request, 'hall_of_shame/debtors.html', context)