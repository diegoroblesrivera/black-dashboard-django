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
        return f"{self.num_run} {self.dv_run} {self.pnombre} {self.snombre} {self.appaterno} {self.apmaterno} {self.nacionalidad} {self.telefono} {self.fecha_nac} {self.id_direccion}"

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
        return f"{self.nombre} {self.ciudad} {self.comuna} {self.direccion} {self.id_horario}"




class Director_Tecnico(models.Model):
    num_run = models.IntegerField()
    dv_run = models.CharField(max_length=1)
    pri_nombre=models.CharField(max_length=20)
    sec_nombre=models.CharField(max_length=20,blank=True)
    pri_apellido=models.CharField(max_length=20)
    sec_apellido=models.CharField(max_length=20,blank=True)
    nacionalidad=models.CharField(max_length=30)
    id_direccion =models.ForeignKey(Direccion, on_delete=models.CASCADE)  
    correo_electronico=models.EmailField(max_length=30,unique=True)
    telefono=models.CharField(max_length=20)
    def __str__(self):
        return f"{self.pri_nombre} {self.pri_apellido} {self.nacionalidad} {self.correo_electronico} {self.telefono}"
    


class Equipo(models.Model):
    id = models.AutoField(primary_key=True) # Es necesario el id acá?
    name = models.CharField(max_length=20)
    puntos=models.IntegerField(default=0)
    id_DT = models.ForeignKey(Director_Tecnico, on_delete=models.CASCADE, related_name="id_DT")
    def __str__(self):
        return f"{self.Id} {self.name} {self.puntos} {self.id_DT}"



class Arbitro(models.Model):
    num_run = models.IntegerField()
    dv_run = models.CharField(max_length=1)
    pnombre = models.CharField(max_length=50)
    snombre = models.CharField(max_length=50)
    appaterno = models.CharField(max_length=50)
    apmaterno = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=50) 
    fecha_nac = models.DateField()
    telefono = models.CharField(max_length=20)
    correo = models.EmailField(max_length=100, unique=True)
    id_direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.num_run} {self.dv_run} {self.pnombre} {self.snombre} {self.appaterno} {self.apmaterno} {self.nacionalidad} {self.fecha_nac} {self.telefono} {self.correo} {self.id_direccion}" 





class Partido(models.Model):
    hora = models.TimeField()
    id_fecha = models.ForeignKey(Fecha_Campeonato, on_delete=models.CASCADE)
    id_cancha = models.ForeignKey(Cancha, on_delete=models.CASCADE)
    equipo_local = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='partido_como_local')
    equipo_visita = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='partido_como_visita')
    id_arbitro = models.ForeignKey(Arbitro, on_delete=models.CASCADE)
    clima = models.CharField(max_length=50)
    observaciones = models.TextField(max_length=500)
    equipo_ganador = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.hora} {self.id_fecha} {self.id_cancha} {self.equipo_local} {self.equipo_visita} {self.id_arbitro} {self.clima} {self.observaciones} {self.equipo_ganador}"



class Estadistica_Jugador_Torneo(models.Model):
    torneo = models.ForeignKey(Torneo, on_delete=models.CASCADE)
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE)
    total_goles =models.IntegerField(default=0)
    total_amarillas = models.IntegerField(default=0)
    total_rojas = models.IntegerField(default=0)

#   class Meta:
#   unique_together= ('torneo', 'jugador')

    def __str__(self):
        return f"{self.jugador} en {self.torneo}"
    



    
class Tarjeta(models.Model):
    TIPO_OPC = [
        ('amarilla', 'Amarilla'),
        ('roja', 'Roja'),
    ]

    partido = models.ForeignKey(Partido, on_delete=models.CASCADE)
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=10, choices=TIPO_OPC)
    minuto = models.IntegerField()
    
    def __str__(self):
        return f"{self.tipo.title()} a {self.jugador} en el minuto {self.minuto}"




class Gol(models.Model):
    partido = models.ForeignKey(Partido, on_delete=models.CASCADE)
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE)
    minuto = models.IntegerField()
    
    def __str__(self):
        return f"Gol de {self.jugador} en el minuto {self.minuto}"