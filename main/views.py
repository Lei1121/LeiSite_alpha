from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import *

# Create your views here.
def fakeapple(request):
    return render_to_response('fakeapple.html')

def zhihu(request):
    return render_to_response('zhihu.html')

def fakemicrosoft(request):
    return render_to_response('fakemicrosoft.html')

def index(request):
    return render_to_response('index.html')

def JD(request):
    return render_to_response('JD.html')
