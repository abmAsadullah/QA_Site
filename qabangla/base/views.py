from django.shortcuts import render


posts = [
	{
		'author' : 'CoreyMS',
		'title' : 'Question 1',
		'content' : 'First Question content',
		'date_posted' : 'May 14, 2020'
	},
	{
		'author' : 'Saad',
		'title' : 'Question 2',
		'content' : 'Second Question content',
		'date_posted' : 'May 15, 2020'
	},
]



def home(request):
	context = {
		'posts': posts
	}
	return render(request, 'qa/qapage.html', context)
#	return render(request, 'base/home.html', context)

def about(request):
	return render(request, 'base/about.html', {'title': 'About'})

