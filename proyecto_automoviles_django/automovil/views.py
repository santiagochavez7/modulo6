from django.shortcuts import render, redirect, get_object_or_404
from .forms import AutomovilForm  # Cambié VehiculoForm a AutomovilForm
from .models import Automovil  # Cambié Vehiculo a Automovil
from django.contrib.auth.decorators import login_required, permission_required

def pagina_principal(request):
    return render(request, 'automovil/pagina_principal.html')  # Cambié 'vehiculo/index.html' a 'automovil/pagina_principal.html'

def nuevo_automovil(request):
    if request.method == "POST":
        form = AutomovilForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pagina_principal')  # Cambié 'index' a 'pagina_principal'
    else:
        form = AutomovilForm()
    return render(request, 'automovil/nuevo_automovil.html', {'form': form})  # Cambié 'add_vehiculo.html' a 'automovil/nuevo_automovil.html'

@login_required
@permission_required('automovil.view_catalogo', raise_exception=True)
def catalogo_automoviles(request):
    automoviles = Automovil.objects.all()
    
    for automovil in automoviles:
        if automovil.precio <= 10000:
            automovil.condicion_precio = 'Bajo'
        elif 10000 < automovil.precio <= 30000:
            automovil.condicion_precio = 'Medio'
        else:
            automovil.condicion_precio = 'Alto'
    
    return render(request, 'automovil/catalogo_automoviles.html', {'automoviles': automoviles})  # Cambié 'lista_vehiculos.html' a 'automovil/catalogo_automoviles.html'

def detalle_automovil(request, id):
    automovil = get_object_or_404(Automovil, id=id)
    return render(request, 'automovil/detalle_automovil.html', {'automovil': automovil})  # Cambié 'vehiculo/detalle_vehiculo.html' a 'automovil/detalle_automovil.html'
