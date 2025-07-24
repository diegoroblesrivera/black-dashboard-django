from django.contrib import admin
from .models import Horario, Cancha, Direccion, Jugador
# Register your models here.
admin.site.register(Horario)
admin.site.register(Cancha)
admin.site.register(Direccion)
admin.site.register(Jugador)