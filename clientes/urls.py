from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.procesar_login_cliente, name='procesar_login_cliente'),
    path('dashboard/', views.dashboard_cliente, name='dashboard_cliente'),
    path('logout/', views.logout_cliente, name='logout_cliente'),
]