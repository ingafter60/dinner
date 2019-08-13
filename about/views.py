from django.shortcuts import render

# Create your views here.

def aboutPage(request):

	context = {
		'navbar' : 'about'
	}

	return render(request, 'About/about.html', context)