from django.contrib import admin




from registros.models import usuario




class Usuario(admin.ModelAdmin):
    list_display=("username", "nombre", "apellido")
    search_fields=("username",)

admin.site.register(usuario, Usuario)
