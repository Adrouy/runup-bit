from django.contrib import admin

from apps.entrenador.models import Plan_entrenamiento, Entrenador
# Register your models here.

admin.site.register(Plan_entrenamiento)
admin.site.register(Entrenador)