from django.views.generic import TemplateView

# Create your views here.
class PaginaInicial(TemplateView):
    template_name = "index.html"

class PaginaLogin(TemplateView):
    template_name = 'login.html'

class PaginaOrcamento(TemplateView):
    template_name = 'orcamento.html'