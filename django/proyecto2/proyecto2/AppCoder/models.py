from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
    
    def __str__(self):
        return f'{self.nombre} - {self.camada}'
    
class Estudiante(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    def __str__(self):
        return f'{self.nombre} - {self.apellido}'
    
class Profesor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    profesion = models.CharField(max_length=50)
    def __str__(self):
        return f'{self.nombre} - {self.apellido} - {self.profesion}'
    
class Entregable(models.Model):
    nombre = models.CharField(max_length=40)
    fechaDeEntrega = models.DateField()
    entregado = models.BooleanField()
    link = models.CharField(max_length=256, null=True)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.nombre} - {self.fechaDeEntrega} - {self.entregado}'