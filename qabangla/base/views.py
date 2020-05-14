from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return HttpResponse("This is base Home Page.")

def about(request):
	return HttpResponse("This is base About Page.")

