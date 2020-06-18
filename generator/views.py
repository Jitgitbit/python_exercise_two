from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
	return HttpResponse('Hello hello ...')

def eggs(request):
	return HttpResponse('Eggs are great!')