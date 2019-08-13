from django.shortcuts import render

# Create your views here.

def contactPage(request):

	context = {
		'navbar' : 'contact'
	}

	return render(request, 'Contact/contact.html', context)