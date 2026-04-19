from django.db import models

class Astronauta(models.Model):
    RANGO_CHOICES = [
        ('novato', 'Novato'),
        ('piloto', 'Piloto'),
        ('comandante', 'Comandante'),
    ]
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    rango = models.CharField(max_length=20, choices=RANGO_CHOICES, default='novato')
    horas_experiencia = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Ingeniero(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    años_experiencia = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Nave(models.Model):
    ESTADO_CHOICES = [
        ('operativa', 'Operativa'),
        ('en_mantenimiento', 'En Mantenimiento'),
        ('retirada', 'Retirada'),
    ]
    nombre = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    capacidad_tripulación = models.PositiveIntegerField()
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='operativa')

    def __str__(self):
        return self.nombre

class Mision(models.Model):
    ESTADO_CHOICES = [
        ('planificada', 'Planificada'),
        ('en_curso', 'En Curso'),
        ('completada', 'Completada'),
        ('fallida', 'Fallida'),
    ]
    nombre_mision = models.CharField(max_length=200)
    fecha_lanzamiento = models.DateField()
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='planificada')
    astronauta = models.ForeignKey(Astronauta, on_delete=models.CASCADE)
    nave = models.ForeignKey(Nave, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_mision

class RegistroExploracion(models.Model):
    NIVEL_RIESGO_CHOICES = [
        ('bajo', 'Bajo'),
        ('medio', 'Medio'),
        ('alto', 'Alto'),
    ]
    planeta_destino = models.CharField(max_length=100)
    descripcion = models.TextField()
    nivel_riesgo = models.CharField(max_length=10, choices=NIVEL_RIESGO_CHOICES, default='bajo')
    mision = models.ForeignKey(Mision, on_delete=models.CASCADE)

    def __str__(self):
        return f"Exploración a {self.planeta_destino}"