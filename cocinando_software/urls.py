from django.contrib import admin
from django.urls import path, include
from clientes.views import login_cliente  # Importamos directamente

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_cliente, name='login'),  # Usamos la raíz para el login manual
    
    path('clientes/', include('clientes.urls')),  # Si luego hay rutas adicionales
]

