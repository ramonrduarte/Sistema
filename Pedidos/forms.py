from django import forms
from .models import Perfil
from .models import Pedido

class PedidoForm(forms.Form):
    perfil = forms.ChoiceField(
        label='Perfil',
        queryset=Perfil.objects.all(),
    )

    perfilpuxador = forms.ChoiceField(
        label='Perfil Puxador',
        queryset=Perfil.objects.all(),
    )

    class Meta:
        model = Pedido
        fields = '__all__'