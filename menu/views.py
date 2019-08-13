from django.shortcuts import render

# Create your views here.

def menuPage(request):

	context = {
		'navbar' : 'menu'
	}

	return render(request, 'Menu/menu.html', context)