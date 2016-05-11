from django.shortcuts import render
from django.views.generic import View
from .forms import SusForm


class Home(View):
    def get(self, request):
        template_name = 'main/suscripcion.html'
        form = SusForm()
        ctx = {'form': form}
        return render(request, template_name, ctx)
