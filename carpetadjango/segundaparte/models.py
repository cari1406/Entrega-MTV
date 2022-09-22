from django.db import models

class Persona(models.Model):
    nombre= models.CharField(max_length=40)
    nacionalidad= models.CharField(max_length=40)
    nacimiento= models.DateField()
    sexo=  models.CharField(max_length=40)

class Contacto(models.Model):
    direccion= models.CharField(max_length=30)
    telefono= models.CharField(max_length=30)
    email= models.EmailField()

class Curso(models.Model):
    nombre= models.CharField(max_length=40)

class Profesor(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    materia= models.CharField(max_length=30)
