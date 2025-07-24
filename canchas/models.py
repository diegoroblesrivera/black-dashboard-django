from django.db import models

# class Director_Tecnico(models.Model):
#     pri_nombre=models.CharField(max_length=20)
#     sec_nombre=models.CharField(max_length=20,blank=True)
#     pri_apellido=models.CharField(max_length=20)
#     sec_apellido=models.CharField(max_length=20,blank=True)
#     nacionalidad=models.CharField(max_length=30)
#     correo_electronico=models.EmailField(max_length=30,unique=True)
#     telefono=models.CharField(max_length=20)


#     def __str__(self):
#         return f"{self.pri_nombre} {self.pri_apellido}"
    
class Horarios(models.Model):
    dia = models.DateField()
    horario_apertura=models.TimeField(blank=True)
    horario_cierre=models.TimeField(blank=True)
    def __str__(self):
        return f"{self.dia} {self.horario_apertura} {self.horario_cierre}"
    


class Torneo(models.Model):
    nombre = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.nombre}"
    

class Fecha_Campeonato(models.Model):
    numero_fecha = models.IntegerField()
    dia_inicio_fecha = models.DateField(blank=True)
    dia_final_fecha = models.DateField(blank=True)
    torneo = models.ForeignKey(Torneo, on_delete=models.CASCADE, related_name="fechas")
    