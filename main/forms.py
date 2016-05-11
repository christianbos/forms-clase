from django import forms
from .models import Suscriptor
from django.utils.translation import ugettext_lazy as _


class SusForm(forms.ModelForm):
    nombre = forms.CharField(widget=forms.Textarea, label={'class': 'rellenito'})

    class Meta:
        model = Suscriptor
        fields = ['nombre', 'email']
        labels = {
                'nombre': _('escribe tu nombre'),
                'email': _('introduce mail')
        }
        widgets = {
            'nombre': forms.Textarea(attrs={'class': 'rellenito'}),
        }
