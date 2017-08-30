from django.contrib import admin
from agenda.models import Evento, Local

from django.conf.locale.en import formats as en_formats
en_formats.DATETIME_FORMAT = "d/m/Y"
# Register your models here.

class EventoAdmin(admin.ModelAdmin):
    list_display = ('data', 'descricao', 'vereador', 'local')

class LocalAdmin(admin.ModelAdmin):
    pass


admin.site.register(Evento, EventoAdmin)
admin.site.register(Local, LocalAdmin)
