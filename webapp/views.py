import socket
import struct

from django.shortcuts import render, redirect

from django.urls import reverse_lazy
from django.views.generic import ListView
from ipware import get_client_ip
from django.views.generic.edit import CreateView, DeleteView

from webapp.forms import ConsultaForm
from webapp.models import *



def index(request):
    return render(request, 'webapp/home.html')


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def cidr_to_netmask(mascara):
    net_bits = int(mascara)
    host_bits = 32 - net_bits
    netmask = socket.inet_ntoa(struct.pack('!I', (1 << 32) - (1 << host_bits)))
    return netmask


def consulta_view(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            a = form.save()
            a.iphost = get_client_ip(request)

            mascara_field = form.cleaned_data['mascara']

            if (int(mascara_field) <= 32) and (int(mascara_field) > 1):
                print(mascara_field)
                a.mascara = str(cidr_to_netmask(mascara_field))
                a.save()

        return redirect('consulta:consulta_listar')

    else:

        form = ConsultaForm()
    return render(request, 'webapp/consulta_form.html', {'form': form})


class ConsultaCreate(CreateView):
    model = Consulta
    form_class = ConsultaForm
    template_name = 'webapp/consulta_form.html'
    success_url = reverse_lazy('')


class ConsultaList(ListView):
    model = Consulta
    template_name = 'webapp/consulta_list.html'


class ConsultaDelete(DeleteView):
    model = Consulta
    template_name = 'webapp/consulta_delete.html'
    success_url = reverse_lazy('consulta:consulta_listar')


def consulta_delete(request, id_consulta):
    consulta = Consulta.objects.get(id=id_consulta)
    if request.method == 'POST':
        consulta.delete()
        return redirect('consulta:consulta_listar')
    return render(request, 'webapp/consulta_delete.html', {'consulta': consulta})


def consulta_list(request):
    consulta = Consulta.objects.all().order_by('id')
    contexto = {'consulta': consulta}
    return render(request, 'webapp/consulta_list.html', contexto)



