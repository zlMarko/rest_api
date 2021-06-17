from django.contrib import admin

from apirest.models import *


class PilotoAdmin(admin.ModelAdmin):
    list_display = ("rut", "nombre", "apellido")
    search_fields = ("rut",)


admin.site.register(Piloto, PilotoAdmin)


class LicenciaAdmin(admin.ModelAdmin):
    list_display = ("n_licencia_piloto",)
    search_fields = ("n_licencia_piloto",)


admin.site.register(Licencia, LicenciaAdmin)

class AeronaveAdmin(admin.ModelAdmin):
    list_display = ("matricula",)
    search_fields = ("matricula",)

admin.site.register(Aeronave, AeronaveAdmin)


class VuelosAdmin(admin.ModelAdmin):
    list_display = ("id"),
    search_fields = ("id"),


admin.site.register(Vuelo, VuelosAdmin)
