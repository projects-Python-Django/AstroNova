from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Astronauta, Ingeniero, Nave, Mision, RegistroExploracion

def home(request):
    context = {
        'astronautas_count': Astronauta.objects.count(),
        'ingenieros_count': Ingeniero.objects.count(),
        'naves_count': Nave.objects.count(),
        'misiones_count': Mision.objects.count(),
        'registros_count': RegistroExploracion.objects.count(),
    }
    return render(request, 'exploracion/home.html', context)

# Astronauta Views
class AstronautaListView(ListView):
    model = Astronauta
    template_name = 'exploracion/astronauta_list.html'
    context_object_name = 'astronautas'

class AstronautaDetailView(DetailView):
    model = Astronauta
    template_name = 'exploracion/astronauta_detail.html'

class AstronautaCreateView(CreateView):
    model = Astronauta
    template_name = 'exploracion/astronauta_form.html'
    fields = ['nombre', 'apellido', 'rango', 'horas_experiencia']
    success_url = reverse_lazy('astronauta_list')

class AstronautaUpdateView(UpdateView):
    model = Astronauta
    template_name = 'exploracion/astronauta_form.html'
    fields = ['nombre', 'apellido', 'rango', 'horas_experiencia']
    success_url = reverse_lazy('astronauta_list')

class AstronautaDeleteView(DeleteView):
    model = Astronauta
    template_name = 'exploracion/astronauta_confirm_delete.html'
    success_url = reverse_lazy('astronauta_list')

# Ingeniero Views
class IngenieroListView(ListView):
    model = Ingeniero
    template_name = 'exploracion/ingeniero_list.html'
    context_object_name = 'ingenieros'

class IngenieroDetailView(DetailView):
    model = Ingeniero
    template_name = 'exploracion/ingeniero_detail.html'

class IngenieroCreateView(CreateView):
    model = Ingeniero
    template_name = 'exploracion/ingeniero_form.html'
    fields = ['nombre', 'apellido', 'especialidad', 'años_experiencia']
    success_url = reverse_lazy('ingeniero_list')

class IngenieroUpdateView(UpdateView):
    model = Ingeniero
    template_name = 'exploracion/ingeniero_form.html'
    fields = ['nombre', 'apellido', 'especialidad', 'años_experiencia']
    success_url = reverse_lazy('ingeniero_list')

class IngenieroDeleteView(DeleteView):
    model = Ingeniero
    template_name = 'exploracion/ingeniero_confirm_delete.html'
    success_url = reverse_lazy('ingeniero_list')

# Nave Views
class NaveListView(ListView):
    model = Nave
    template_name = 'exploracion/nave_list.html'
    context_object_name = 'naves'

class NaveDetailView(DetailView):
    model = Nave
    template_name = 'exploracion/nave_detail.html'

class NaveCreateView(CreateView):
    model = Nave
    template_name = 'exploracion/nave_form.html'
    fields = ['nombre', 'modelo', 'capacidad_tripulación', 'estado']
    success_url = reverse_lazy('nave_list')

class NaveUpdateView(UpdateView):
    model = Nave
    template_name = 'exploracion/nave_form.html'
    fields = ['nombre', 'modelo', 'capacidad_tripulación', 'estado']
    success_url = reverse_lazy('nave_list')

class NaveDeleteView(DeleteView):
    model = Nave
    template_name = 'exploracion/nave_confirm_delete.html'
    success_url = reverse_lazy('nave_list')

# Mision Views
class MisionListView(ListView):
    model = Mision
    template_name = 'exploracion/mision_list.html'
    context_object_name = 'misiones'

class MisionDetailView(DetailView):
    model = Mision
    template_name = 'exploracion/mision_detail.html'

class MisionCreateView(CreateView):
    model = Mision
    template_name = 'exploracion/mision_form.html'
    fields = ['nombre_mision', 'fecha_lanzamiento', 'estado', 'astronauta', 'nave']
    success_url = reverse_lazy('mision_list')

class MisionUpdateView(UpdateView):
    model = Mision
    template_name = 'exploracion/mision_form.html'
    fields = ['nombre_mision', 'fecha_lanzamiento', 'estado', 'astronauta', 'nave']
    success_url = reverse_lazy('mision_list')

class MisionDeleteView(DeleteView):
    model = Mision
    template_name = 'exploracion/mision_confirm_delete.html'
    success_url = reverse_lazy('mision_list')

# RegistroExploracion Views
class RegistroExploracionListView(ListView):
    model = RegistroExploracion
    template_name = 'exploracion/registroexploracion_list.html'
    context_object_name = 'registros'

class RegistroExploracionDetailView(DetailView):
    model = RegistroExploracion
    template_name = 'exploracion/registroexploracion_detail.html'

class RegistroExploracionCreateView(CreateView):
    model = RegistroExploracion
    template_name = 'exploracion/registroexploracion_form.html'
    fields = ['planeta_destino', 'descripcion', 'nivel_riesgo', 'mision']
    success_url = reverse_lazy('registroexploracion_list')

class RegistroExploracionUpdateView(UpdateView):
    model = RegistroExploracion
    template_name = 'exploracion/registroexploracion_form.html'
    fields = ['planeta_destino', 'descripcion', 'nivel_riesgo', 'mision']
    success_url = reverse_lazy('registroexploracion_list')

class RegistroExploracionDeleteView(DeleteView):
    model = RegistroExploracion
    template_name = 'exploracion/registroexploracion_confirm_delete.html'
    success_url = reverse_lazy('registroexploracion_list')