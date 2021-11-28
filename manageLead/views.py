from django.shortcuts import render

# Create your views here.


def showLeads(request):
    return render(request, 'showleads.html')
