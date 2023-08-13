from django.db import models



class Paciente(models.Model):
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    email = models.EmailField()
    telefono = models.IntegerField()

    def __Str__(self):
        return self.fk_medico.especialidad
    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'


class Clinica(models.Model):
    direccion = models.TextField()
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Clinica'
        verbose_name_plural = 'Clinicas'


class Medico(models.Model):
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    email = models.EmailField()
    especialidad = models.CharField(max_length=200)
    telefono = models.IntegerField()
    fk_clinica =models.ForeignKey(Clinica, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Medico'
        verbose_name_plural = 'Medicos'


class Adminostrador(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    fk_clinica =models.ForeignKey(Clinica, on_delete=models.CASCADE)



    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Administrador'
        verbose_name_plural = 'Administradores'

class Jornada(models.Model):
    fecha = models.DateField()
    horaEntrada = models.TimeField()
    horaSalida = models.TimeField()
    horasExtras = models.IntegerField()
    fk_clinica =models.ForeignKey(Clinica, on_delete=models.CASCADE)



    def __str__(self):
        return self.fk_clinica.direccion
    
    class Meta:
        verbose_name = 'Jormada'
        verbose_name_plural = 'Jornadas'