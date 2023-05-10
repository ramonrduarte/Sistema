from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/login/', auth_view.LoginView.as_view(), name='login'),
    path('account/logout/', auth_view.LogoutView.as_view(), name='logout'),
    path('', include('paginas.urls')),
    path('', include('cadastros.urls')),
    path('', include('Clientes.urls')),

]
