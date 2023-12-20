from django import forms
from .models import Perfil, Pedido


class PedidoForm(forms.ModelForm):
    perfil = forms.ChoiceField(
        label='Perfil',
        queryset=Perfil.objects.all(),
    )

    class Meta:
        model = Pedido
        fields = '__all__'
