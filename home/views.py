from django.shortcuts import render

# Create your views here.

def homePage(request):

	context = {
		'navbar' : 'home'
	}

	return render(request, 'Home/index.html', context)