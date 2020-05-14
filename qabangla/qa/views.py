from django.shortcuts import render
from django.http import HttpResponse

def qa(request):
	return HttpResponse("This is qa page")