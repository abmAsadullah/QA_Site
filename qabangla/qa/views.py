from django.shortcuts import render
from .models import Post


def qa(request):
	cont = {
		'posts': Post.objects.all()
	}
	return render(request, 'qa/qapage.html', cont)