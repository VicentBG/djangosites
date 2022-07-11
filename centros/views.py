from django.shortcuts import render, get_object_or_404, redirect
from .models import Bono
from .forms import BonoForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='nuevo_bono')
def lista_bonos(request):
    bonos = Bono.objects.all()
    return render(request, 'centros/lista_bonos.html', {'bonos': bonos})

@login_required(login_url='nuevo_bono')
def detalle_bono(request, pk):
    bono = get_object_or_404(Bono, pk=pk)
    return render(request, 'centros/detalle_bono.html', {'bono': bono})

def nuevo_bono(request):
    if request.method == "POST":
        form = BonoForm(request.POST)
        if form.is_valid():
            bono = form.save(commit=False)
            bono.save()
            return redirect('nuevo_bono')
    else:
        form = BonoForm()
    return render(request, 'centros/edita_bono.html', {'form': form})

@login_required(login_url='nuevo_bono')
def edita_bono(request, pk):
    bono = get_object_or_404(Bono, pk=pk)
    if request.method == "POST":
        form = BonoForm(request.POST, instance=bono)
        if form.is_valid():
            bono = form.save(commit=False)
            bono.save()
            return redirect('detalle_bono', pk=bono.pk)
    else:
        form = BonoForm(instance=bono)
    return render(request, 'centros/edita_bono.html', {'form': form})
