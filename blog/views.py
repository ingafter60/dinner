from django.shortcuts import render

# Create your views here.

def blogPage(request):

	context = {
		'navbar' : 'blog'
	}

	return render(request, 'Blog/blog.html', context)