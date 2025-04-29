from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.procesar_login_cliente, name='procesar_login_cliente'),
    path('dashboard/', views.dashboard_cliente, name='dashboard_cliente'),
    path('listado/', views.listado_clientes, name='listado_clientes'), 
    path('crear/', views.crear_cliente, name='crear_cliente'),
    path('editar/<int:cliente_id>/', views.editar_cliente, name='editar_cliente'),
    path('eliminar/<int:cliente_id>/', views.eliminar_cliente, name='eliminar_cliente'),
    path('logout/', views.logout_cliente, name='logout_cliente'),
]