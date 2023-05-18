from django import forms
from .models import Perfil, PerfilPuxador, Puxador, ENCAIXE
from django.views.generic.edit import CreateView

class PerfilForm(forms.ModelForm):

    encaixe = forms.ChoiceField(
        label='Permite Perfil Puxador?',
        choices=ENCAIXE,
        widget=forms.RadioSelect
        )
    encaixepuxador = forms.ChoiceField(
        label='Permite Puxador?',
        choices=ENCAIXE,
        widget=forms.RadioSelect
    )
    puxadorsobreposto = forms.ModelMultipleChoiceField(
        label='Puxadores',
        queryset=Puxador.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required = False,
    )

    class Meta:
        model = Perfil
        fields = '__all__'


