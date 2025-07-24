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
