from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def captain(request):
    return HttpResponse('<h1>shreyas iyyer captain of panjab kings team</h1>')
