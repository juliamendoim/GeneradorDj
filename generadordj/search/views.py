from django.shortcuts import render
from .models import Lexico
from django.http import HttpResponse


def searchlex(request):
    hola = Lexico.objects.all().order_by('id')
    return render(request,'search.html', {'hola':hola})
# Create your views here.
