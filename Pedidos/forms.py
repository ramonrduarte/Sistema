from django import forms
from django_select2.widgets import Select2Widget
from .models import Pedido

class PedidoForm(forms.Form):
    perfil = forms.ChoiceField(
        label='Perfil',
        queryset=Perfil.objects.all(),
        widget=Select2Widget,
    )

    class Meta:
        model = Pedido
        fields = '__all__'