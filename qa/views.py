from django.shortcuts import render
from .models import Question


def qa(request):
	cont = {
		'questions': Question.objects.all()
	}
	return render(request, 'qa/qapage.html', cont)