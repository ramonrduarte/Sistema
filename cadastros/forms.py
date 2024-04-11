from django import forms
from .models import Perfil, PerfilPuxador, Puxador, ENCAIXE, Divisor


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
    puxador = forms.ModelMultipleChoiceField(
        label='Puxadores',
        queryset=Puxador.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
    perfil_puxador = forms.ModelMultipleChoiceField(
        label='Perfil Puxador',
        queryset=PerfilPuxador.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    vidropolido = forms.BooleanField(label='Vidro Polido', required=False)

    class Meta:
        model = Perfil
        fields = '__all__'
