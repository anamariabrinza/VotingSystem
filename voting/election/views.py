from django.shortcuts import render, redirect
from django.shortcuts import reverse
from .forms import ElectionForm, ChoiceForm
from .models import Election
from django.views import View

# Create your views here.

class MainPage(View):

    def get(self, request):
        return render(request, 'main.html')

class ElectionList(View): #page of elections

    def get(self, request):
        elections = Election.objects.filter(status=0)
        return render(request, 'home.html', {'elections': elections})

    def post(self, request):
        pass
class ElectionDetail(View):
    def get(self, request, pk):
        election_id = Election.objects.get(pk=pk)
        return render(request, 'elections/election_detail.html', {'election':election_id})
    def post(self, request):
        pass

# We need here to add the option of a election
# optionName from ElectionChoices
# there can be 2 ore even more options per election
class CreateElection(View): # creating a new election only by administration and EC

    def get(self, request):
        election_form = ElectionForm()
        return render(request, 'elections/create_election.html', {'election_form': election_form})

    def post(self, request):
        election_form = ElectionForm(request.POST)
        if election_form.is_valid():
            election_form.save()
            return redirect(reverse('election:election-name'))
        else:
            return render(request, 'elections/create_election.html', {'election_form': election_form})

