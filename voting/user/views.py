from django.shortcuts import render
from election.models import Election
from django.views import View
# Create your views here.


def home(request):
    if request.method == 'GET':
        elections = Election.objects.filter(status=0)
        return render(request, 'templates/home.html', {'elections': elections})
    if request.method == 'POST':
        pass





    # creaza functii + logica + return la HTTPResponse
    #creare utilizator
    #logarea