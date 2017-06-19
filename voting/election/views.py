from django.db import transaction
from django.shortcuts import render, redirect
from django.shortcuts import reverse
from django.forms.formsets import formset_factory
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import ElectionForm, ChoiceForm, ChoiceFormSet
from .models import Election, ElectionChoices
from django.views import View

# Create your views here.


class MainPage(View):

    def get(self, request):
        return render(request, 'main.html')


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

    def post(self, request):
        pass


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
