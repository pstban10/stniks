from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic import ListView
from .models import Persona, PrData
from .forms import PrDataForm


def profile(request):

    perfil = get_object_or_404(Persona, user=request.user)

    return render(
        request,
        'data/profile.html',
        {'perfil': perfil}
    )


class RecordsListView(ListView):
    model = PrData
    template_name = 'data/records.html'


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
