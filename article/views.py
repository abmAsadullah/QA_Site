from django.shortcuts import render
from .models import Article



def article(request):
	context = {
		'articles': Article.objects.all()
	}
	return render(request, 'article/articlepage.html', context)