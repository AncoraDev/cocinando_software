from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from .models import Cliente

# Mostrar formulario de login
def login_cliente(request):
    return render(request, 'clientes/login.html')

# Procesar el login del cliente
def procesar_login_cliente(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard_cliente')
        else:
            messages.error(request, 'Email o contraseña incorrectos')

    return redirect('login')

# Dashboard privado del cliente
@login_required
def dashboard_cliente(request):
    try:
        cliente = Cliente.objects.get(user=request.user)
    except Cliente.DoesNotExist:
        return redirect('login')

    return render(request, 'clientes/dashboard.html', {
        'cliente': cliente,
        'active': 'dashboard'
    })

# Listado de todos los clientes
@login_required
def listado_clientes(request):
    try:
        cliente = Cliente.objects.get(user=request.user)
    except Cliente.DoesNotExist:
        return redirect('login')

    clientes = Cliente.objects.all()
    return render(request, 'clientes/listado.html', {
        'clientes': clientes,
        'cliente': cliente,
        'active': 'clientes'
    })

# Crear un nuevo cliente
@login_required
def crear_cliente(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        razon_social = request.POST.get('razon_social')
        cif = request.POST.get('cif')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.create_user(
            username=email,
            email=email,
            password=password,
            first_name=nombre
        )

        Cliente.objects.create(
            user=user,
            razon_social=razon_social,
            cif=cif
        )

        return redirect('listado_clientes')

    return render(request, 'clientes/formulario.html', {'modo': 'crear'})

# Editar un cliente existente
@login_required
def editar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        razon_social = request.POST.get('razon_social')
        cif = request.POST.get('cif')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Actualizar datos del User asociado
        cliente.user.first_name = nombre
        cliente.user.username = email
        cliente.user.email = email
        if password:
            cliente.user.set_password(password)
        cliente.user.save()
        update_session_auth_hash(request, cliente.user) 

        # Actualizar datos de Cliente
        cliente.razon_social = razon_social
        cliente.cif = cif
        cliente.save()

        return redirect('listado_clientes')

    return render(request, 'clientes/formulario.html', {
        'cliente': cliente,
        'modo': 'editar'
    })

# Eliminar un cliente
@login_required
def eliminar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    cliente.user.delete()  # Eliminamos también el User asociado automáticamente
    return redirect('listado_clientes')

# Logout del cliente
@login_required
def logout_cliente(request):
    logout(request)
    return redirect('login')
