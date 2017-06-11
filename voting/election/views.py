from django.shortcuts import render, redirect
from django.shortcuts import reverse
from django.forms.formsets import formset_factory
from .forms import ElectionForm, ChoiceForm
from .models import Election, ElectionChoices
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

    # Create the formset, specifying the form and formset we want to use.

    def get(self, request):

        election_form = ElectionForm()
        choice_form = ChoiceForm()
        context = {
            'election_form': election_form,
            'choice_form': choice_form,
        }
        return render(request, 'elections/create_election.html', context)

    def post(self, request):
        #ChoiceFormSet = formset_factory(ChoiceForm)

        election_form = ElectionForm(request.POST, instance=Election())
        choice_form = [ChoiceForm(request.POST, prefix=str(x), instance=ElectionChoices())for x in range(0, 3)]

        if election_form.is_valid() and all([cf.is_valid() for cf in choice_form]):
            new_election = election_form.save()

            for cf in choice_form:
                new_choice = cf.save(commit=False)
                new_choice.election_id = new_election
                new_choice.save()

            return redirect(reverse('election:election-name'))
        else:
            return render(request, 'elections/create_election.html', {
                'election_form': election_form,
                'choice_formset': choice_form,
            })

