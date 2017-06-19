from django.db import transaction
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import reverse
from django.forms.formsets import formset_factory
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

from .forms import ElectionForm, ChoiceForm, ChoiceFormSet
from .models import Election, ElectionChoices
from django.views import View

# Create your views here.


class MainPage(View):

    def get(self, request):
        return render(request, 'main.html')


class ThanksPage(View):

    def get(self, request):
        return render(request, 'success.html')

    def post(self, request):
        pass


class ElectionList(LoginRequiredMixin, View): #page of election

    def get(self, request):
        elections = Election.objects.filter(status=0)
        return render(request, 'home.html', {'elections': elections})

    def post(self, request):
        pass


class ElectionDetail(LoginRequiredMixin, View):
    def get(self, request, pk):
        election_id = Election.objects.get(pk=pk)
        return render(request, 'election/election_detail.html', {'election':election_id})

    def vote(self, request, pk):
        election = get_object_or_404(Election, pk=pk)
        try:
            selected_choice = election.electionchoices_set.get(pk=request.POST['electionchoices'])
        except (KeyError, ElectionChoices.DoesNotExist):
            # Redisplay the question voting form.
            return render(request, 'election/election_detail.html', {
                'election': election,
                'error_message': "You didn't select a choice.",
            })
        else:
            selected_choice += 1
            selected_choice.save()
            # Always return an HttpResponseRedirect after successfully dealing
            # with POST data. This prevents data from being posted twice if a
            # user hits the Back button.
            return HttpResponseRedirect(reverse('election:election-detail', args=(election.id,)))


class CreateElection(LoginRequiredMixin, CreateView): # creating a new election only by administration and EC
    model = Election
    fields = ['name', 'description', 'startDate', 'endDate', 'status', 'group']
    success_url = reverse_lazy('election:election-name')

    def get_context_data(self, **kwargs):
        data = super(CreateElection,self).get_context_data(**kwargs)
        if self.request.POST:
            data['electionchoices'] = ChoiceFormSet(self.request.POST)
        else:
            data['electionchoices'] = ChoiceFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        electionchoices = context['electionchoices']
        with transaction.atomic():
            self.object = form.save()

            if electionchoices.is_valid():
                electionchoices.instance = self.object
                electionchoices.save()
        return super(CreateElection, self).form_valid(form)
