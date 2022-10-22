from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

def index(request):
    links = ['', 'polls', 'admin', 'test', ]
    context = {
        'links': links,
    }
    return render(request, 'index/index.html', context)
