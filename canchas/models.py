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

class Direccion(models.Model):
    nombre_calle = models.CharField(max_length=100)
    num_calle = models.IntegerField()
    comuna = models.CharField(max_length=100)
    region = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre_calle} #{self.num_calle}, {self.comuna}, {self.region}"


class Jugador(models.Model):
    num_run = models.IntegerField()
    dv_run = models.CharField(max_length=1)
    pnombre = models.CharField(max_length=50)
    snombre = models.CharField(max_length=50, blank=True)
    appaterno = models.CharField(max_length=50)
    apmaterno = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=50)
    telefono = models.IntegerField()
    fecha_nac = models.DateField()
    id_direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.pnombre} {self.appaterno}"

class Horario(models.Model):
    dia = models.DateField()
    horario_apertura=models.TimeField()
    horario_cierre=models.TimeField()
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
    def __str__(self):
        return f"{self.numero_fecha} {self.dia_inicio_fecha} {self.dia_final_fecha}"

    
class Cancha(models.Model):
    nombre=models.CharField(max_length=50,unique=True)
    ciudad=models.CharField(max_length=50)
    comuna=models.CharField(max_length=30)
    direccion=models.CharField(max_length=30, unique=True)
    id_horario=models.ManyToManyField(Horario)
    def __str__(self):
        return self.nombre
