from django.contrib import admin
from politicos.models import Politico, Partido

# Register your models here.
class PoliticoAdmin(admin.ModelAdmin):
    pass

class PartidoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Politico, PoliticoAdmin)
admin.site.register(Partido, PartidoAdmin)