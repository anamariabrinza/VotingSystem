from django import forms
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
        exclude = ('election_id',)

    """
    Form for election choices
   

    option = forms.CharField(
                    max_length=100,
                    widget=forms.TextInput(attrs={
                        'placeholder': 'Election choice/option',
                    }),
                    required=False)  """