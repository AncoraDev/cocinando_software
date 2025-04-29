from django.shortcuts import render, redirect
from .models import Cliente
from django.contrib import messages


def login_cliente(request):
    return render(request, 'clientes/login.html')

def procesar_login_cliente(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            cliente = Cliente.objects.get(email=email)
            if cliente.password == password:
                request.session['cliente_id'] = cliente.id
                return redirect('/clientes/dashboard/')
            else:
                messages.error(request, 'Contraseña incorrecta')
        except Cliente.DoesNotExist:
            messages.error(request, 'No existe ningún cliente con ese email')

    return redirect('/')  # Volver al login si algo falla

def dashboard_cliente(request):
    cliente_id = request.session.get('cliente_id')
    if not cliente_id:
        return redirect('login_cliente')
    
    cliente = Cliente.objects.get(id=cliente_id)
    return render(request, 'clientes/dashboard.html', {'cliente': cliente})


def logout_cliente(request):

    print("Cerrando sesión del cliente")
    try:
        del request.session['cliente_id']
    except KeyError:
        pass
    return redirect('/')
