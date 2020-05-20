from django.shortcuts import render
from .models import Test

def tst(request):
	context = {
		'tests': Test.objects.all()
	}
	return render(request, 'tst/tstpage.html', context)





	