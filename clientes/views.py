from django.shortcuts import render, redirect
from .models import Cliente
from django.contrib import messages
from django.shortcuts import get_object_or_404

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
    return render(request, 'clientes/dashboard.html', {
        'cliente': cliente,
        'active': 'dashboard'
    })

def listado_clientes(request):
    cliente_id = request.session.get('cliente_id')
    if not cliente_id:
        return redirect('login')

    cliente = Cliente.objects.get(id=cliente_id)
    clientes = Cliente.objects.all()
    return render(request, 'clientes/listado.html', {
        'clientes': clientes,
        'cliente': cliente,
        'active': 'clientes'
    })


def crear_cliente(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        razon_social = request.POST.get('razon_social')
        cif = request.POST.get('cif')
        email = request.POST.get('email')
        password = request.POST.get('password')

        Cliente.objects.create(
            nombre=nombre,
            razon_social=razon_social,
            cif=cif,
            email=email,
            password=password
        )
        return redirect('listado_clientes')

    return render(request, 'clientes/formulario.html', {'modo': 'crear'})

def editar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)

    if request.method == 'POST':
        cliente.nombre = request.POST.get('nombre')
        cliente.razon_social = request.POST.get('razon_social')
        cliente.cif = request.POST.get('cif')
        cliente.email = request.POST.get('email')
        cliente.password = request.POST.get('password')
        cliente.save()
        return redirect('listado_clientes')

    return render(request, 'clientes/formulario.html', {'cliente': cliente, 'modo': 'editar'})


def eliminar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    cliente.delete()
    return redirect('listado_clientes')

def logout_cliente(request):

    print("Cerrando sesión del cliente")
    try:
        del request.session['cliente_id']
    except KeyError:
        pass
    return redirect('/')
