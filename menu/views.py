from django.shortcuts import render
from .models import Menu
# Create your views here.

# Display all menus
def menuList(request):
	# Get all the menu objects
	menuList = Menu.objects.all()

	context = {
		'navbar' : 'menu',
		'menuList' : menuList
	}

	return render(request, 'Menu/menulist.html', context)

# Display detail menu
def menuDetail(request, slug):
	# Get all the menu objects
	menuDetail = Menu.objects.get(slug=slug)

	context = {
		'navbar' : 'menu',
		'menuDetail' : menuDetail
	}

	return render(request, 'Menu/menudetail.html', context)