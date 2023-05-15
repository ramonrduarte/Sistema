from django import forms
from .models import Perfil, PerfilPuxador, Puxador, ENCAIXE

class PerfilForm(forms.ModelForm):

    encaixe = forms.ChoiceField(
        label='Permite encaixe de Perfil Puxador?',
        choices=ENCAIXE,
        widget=forms.RadioSelect
        )
    encaixepuxador = forms.ChoiceField(
        label='Permite encaixe de Puxador?',
        choices=ENCAIXE,
        widget=forms.RadioSelect
    )
    puxadorsobreposto = forms.ModelMultipleChoiceField(
        queryset=Puxador.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Perfil
        fields = '__all__'
