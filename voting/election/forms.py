from django import forms
from django.forms import inlineformset_factory

from .models import Election, ElectionChoices


class ElectionForm(forms.ModelForm):

    class Meta:
        model = Election
        exclude = ()

# asta cumva trebuie de inclus pe pagina Create Election
# Adaugam optiunile de vot, 2 sau mai multe
# optionName from ElectionChoices

class ChoiceForm(forms.ModelForm):

    class Meta:
        model = ElectionChoices
        exclude = ()

ChoiceFormSet = inlineformset_factory(Election, ElectionChoices, form=ChoiceForm, extra=1)
