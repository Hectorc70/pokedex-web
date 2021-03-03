from django import forms

from .models import Pokemon

class RegistroForm(forms.Form):
    username = forms.CharField(min_length=4, max_length=15,
                                required=True, widget=forms.TextInput)
    email = forms.EmailField(max_length=30, required=True,
                            widget=forms.TextInput)
    password = forms.CharField(max_length=8, required=True,
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmacion de Password', max_length=8,
                                widget=forms.PasswordInput)




class PokemonForm(forms.ModelForm):

    class Meta:
        model = Pokemon
        fields = '__all__'