from django.contrib import admin

from .models import Juego
# Register your models here.

class JuegoAdmin(admin.ModelAdmin):
	list_display = ('tituloJuego', 'fechaLanzamiento', 'generoJuego', 'plataformaJuego')
	list_filter = ['plataformaJuego']
	search_fields = ['tituloJuego']

admin.site.register(Juego, JuegoAdmin)