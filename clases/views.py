from django.http import JsonResponse
from django.shortcuts import redirect, render
from .forms import TestClassForm
from .models import Hours
# Create your views here.


def index(request):
    return render(
        request,
        'inicio.html'
    )


def horarios(request):
    dia = request.GET.get('dia')
    horas = Hours.objects.filter(weekday=dia).values_list('hour', flat=True)
    return JsonResponse({'horarios': list(horas)})


def clase_de_prueba(request):

    data = {
        'form': TestClassForm()
    }
    if request.method == 'POST':
        formulario = TestClassForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data['form'] = formulario
            return redirect('inicio')

    return render(
        request,
        'reservar.html',
        data
    )
