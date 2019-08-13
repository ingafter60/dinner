from django.shortcuts import render

# Create your views here.

def reservationPage(request):

	context = {
		'navbar' : 'reservation'
	}

	return render(request, 'Reservation/reservation.html', context)