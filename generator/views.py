from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
	return render(request, 'generator/home.html')

def eggs(request):
	return HttpResponse('<h1>Eggs are great!</h1>')

def password(request):

	characters = list('abcdefghijklmnopqrstuvwxyz')

	length = 10

	thePassword = ''
	for x in range(length):
		thePassword += random.choice(characters)

	return render(request, 'generator/password.html', {'password': thePassword})