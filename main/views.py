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

def jspractice(request):
    return render_to_response('jspractice.html')

def Carousellianxi(request):
    return render_to_response('Carousellianxi.html')

def school(request):
    return render_to_response('school.html')

def donut(request):
    return render_to_response('donut.html')

def BeijingMore(request):
    return render_to_response('BeijingMore.html')

def food(request):
    return render_to_response('food.html')

def music(request):
    return render_to_response('music.html')

def calculator(request):
    return render_to_response('calculator.html')

