from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic import ListView
from .models import PrData, Usuario
from .forms import PrDataForm, PersonaForm
from django.http import JsonResponse
from django.views.decorators.http import require_GET


def profile(request):

    perfil = get_object_or_404(Usuario, user=request.user)

    return render(
        request,
        'data/profile.html',
        {'perfil': perfil}
    )


class RecordsListView(ListView):
    model = PrData
    template_name = 'data/records.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = sorted(
            queryset, key=lambda record: record.maxRepParalelDips(), reverse=True)
        return [record for record in queryset if record.maxRepParalelDips()]


@require_GET
def filter_records(request):
    query = request.GET.get('query', '').lower()
    filtered_records = PrData.objects.filter(user__name__icontains=query)
    records_data = [
        {'user': record.user.name,
         'pull_up': record.pull_up,
         'pull_up_weight': record.pull_up_weight,
         'pull_up_rm': record.maxRepPullUp(),
         'paralel_dips': record.paralel_dips,
         'paralel_dips_weight': record.paralel_dips_weight,
         'paralel_dips_rm': record.maxRepParalelDips(),
         } for record in filtered_records
    ]
    return JsonResponse({'records': records_data})


def edit_record(request, pk):
    record = get_object_or_404(PrData, pk=pk)
    if request.method == 'POST':
        form = PrDataForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('records'))
    else:
        form = PrDataForm(instance=record)
    return render(request, 'data/edit_record.html', {'form': form})


def add_user(request):
    if request.method == 'POST':

        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('records')
    else:
        form = PersonaForm()
    return render(
        request,
        'data/add_Persona.html',
        {'form': form}
    )


def add_record(request):
    if request.method == 'POST':
        form = PrDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('records')  # Redirige a la lista de registros
    else:
        form = PrDataForm()
    return render(
        request,
        'data/create_record.html',
        {'form': form}
    )
