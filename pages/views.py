from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.


def index(request):
    return render(request, 'pages/index.html', {'name': 'test!!!'})

def details(request, id):
    return HttpResponse(f'page id is {id}')