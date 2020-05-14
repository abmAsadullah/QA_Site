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
	{
		'author' : 'Hasanat',
		'title' : 'Question 3',
		'content' : 'Third Question content',
		'date_posted' : 'May 16, 2020'
	},
]




def qa(request):
	cont = {
		'posts': posts
	}
	return render(request, 'qa/qapage.html', cont)