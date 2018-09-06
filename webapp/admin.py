from django.contrib import admin

# Register your models here.
from django.contrib import admin
from webapp.models import Consulta

class ModelAdmin(admin.ModelAdmin):
    pass
admin.site.register(Consulta, ModelAdmin)