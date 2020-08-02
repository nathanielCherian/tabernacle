from django import forms
from .models import Person

class PersonCreateForm(forms.ModelForm):
    #name = forms.CharField(widget=forms.TextInput, required=False)
    #email = forms.CharField(widget=forms.TextInput, required=False)


    class Meta:
        model = Person
        fields = ('name', 'email', 'phone')