from django.db import models

# Create your models here.
class Course(models.Model):
    code = models.CharField(max_length=150)
    name = models.CharField(max_length=50)
    hour = models.DecimalField(max_digits=3, decimal_places=2)
    state = models.BooleanField(default=True)
    # auto_now_add=True me pertmite
    # registrar la fecha de creación del registro
    creado = models.DateTimeField(auto_now_add=True)
    # auto_now=True me permite registrar
    # la fecha cuando se modifique el registro
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        
        return "Curso : " + self.name + "/ Creditos: "+self.credits
    
    
    
class Career(models.Model):
    name = models.CharField(max_length=50)
    shortname = models.CharField(max_length=20)
    imagen = models.ImageField(
        default='null', verbose_name="Miniatura", upload_to="Career")
    state = models.BooleanField(default=True)
    # auto_now_add=True me pertmite
    # registrar la fecha de creación del registro
    creado = models.DateTimeField(auto_now_add=True)
    # auto_now=True me permite registrar
    # la fecha cuando se modifique el registro
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Carrera : " + self.name + "/ Creditos: "+self.shortname
