from django import forms
from .models import Perfil, PerfilPuxador, Puxador, ENCAIXE, Acabamento, Divisor, Vidro
from django.views.generic.edit import CreateView
from django.urls import reverse

class PerfilForm(forms.ModelForm):

    encaixe = forms.ChoiceField(
        label='Perfil Puxador?',
        choices=ENCAIXE,
        widget=forms.RadioSelect,
    )
    encaixepuxador = forms.ChoiceField(
        label='Permite Puxador?',
        choices=ENCAIXE,
        widget=forms.RadioSelect
    )
    encaixedivisor = forms.ChoiceField(
        label='Permite Divisor?',
        choices=ENCAIXE,
        widget=forms.RadioSelect,
    )
    divisor = forms.ModelMultipleChoiceField(
        label='Divisor',
        queryset=Divisor.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
    puxadorsobreposto = forms.ModelMultipleChoiceField(
        label='Puxadores',
        queryset=Puxador.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required = False,
    )
    perfil_puxador = forms.ModelMultipleChoiceField(
        label='Perfil Puxador',
        queryset=PerfilPuxador.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )


    class Meta:
        model = Perfil
        fields = '__all__'
