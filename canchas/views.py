from django.shortcuts import render, redirect
from .forms import HorarioForm

def test(request):
    
    # Page from the theme 
    return render(request, 'test/index.html')

def crear_horario(request):
    if request.method == 'POST':
        form = HorarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_horarios')  # Redirecciona a donde quieras
    else:
        form = HorarioForm()
    
    return render(request, 'test/horario_form.html', {'form': form})
