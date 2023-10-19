from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic
from reserva.models import Reserva
from stand.models import Stand

# Create your views here.
class HomeView(LoginRequiredMixin, generic.TemplateView):
    template_name = "core/index.html"

class ProfileView(LoginRequiredMixin, generic.TemplateView):
    template_name = "account/profile.html"

class ReservaDetailView(generic.DetailView):
    model = Reserva
    template_name = "core/detalhe.html"

class StandDetailView(generic.DetailView):
    model = Stand
    template_name = "core/detalhestand.html"