from django.forms import ModelForm

from webapp import admin
from webapp.models import Consulta


class ConsultaForm(ModelForm):
    class Meta:
        model = Consulta

        fields = ['objetivo', 'mascara']

        labels = {
            'objetivo': 'Objetivo',
            'mascara': 'Mascara',

        }


class ConsultaAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha', 'hora','estado')
    form = ConsultaForm
