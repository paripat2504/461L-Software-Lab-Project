from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .databasescript import GetParsedPlatformList, BootParserEntry
from django.http import Http404
from django.shortcuts import render, HttpResponseRedirect
import sys

def homeView(request):
    if request.method == 'POST':
        passToBackEnd = request.POST['passToBackEnd']
        passToFrontEnd = FunctionFromDatabasescrpit(passToBackEnd)
    return render(request, "softwareApp/homeView.html", {
        'passToFrontEnd': passToFrontEnd
    })

# Create your views here.
