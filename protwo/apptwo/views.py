from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<em><h1> my second project<h1></em>")
# Create your views here.
