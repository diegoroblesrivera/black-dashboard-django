from django.contrib import admin

# Register your models here.
from .models import Horario, Cancha, Direccion, Jugador ,Director_Tecnico, Fecha_Campeonato, Torneo, Estadistica_Jugador_Torneo, Tarjeta, Gol
# Register your models here.
admin.site.register(Horario)
admin.site.register(Cancha)
admin.site.register(Direccion)
admin.site.register(Jugador)
admin.site.register(Director_Tecnico)
admin.site.register(Fecha_Campeonato)
admin.site.register(Torneo)
admin.site.register(Estadistica_Jugador_Torneo)
admin.site.register(Tarjeta)
admin.site.register(Gol)