from django.shortcuts import render
from django.utils import timezone
from qa.models import Question as Post
from tst.models import Test
from article.models import Article



def home(request):
	#Want to sow post according to timezone
	# Post = Question or Test or Article
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'base/home.html', context)

def about(request):
	return render(request, 'base/about.html', {'title': 'About'})

