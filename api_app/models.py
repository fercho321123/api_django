from django.db import models
from django.utils.html import MAX_URL_LENGTH
from django.db import models


class Persona(models.Model):
    id_persona = models.AutoField(primary_key=True ,editable=False, db_column='T001IdPersona')
    nombre = models.CharField(  max_length=100, db_column='t001Nombre')
    apellido = models.CharField(  max_length=100, db_column='t001Apellido')
    documento = models.CharField(  max_length=100, db_column='t001Documento')
    email = models.CharField(  max_length=100, db_column='t001Email')
    activo = models.CharField(  max_length=100, db_column='t001Activo')

    def _str_(self):
        return f"{self.nombre}{self.apellido}"

    class Meta:
        db_table = 'T001Persona'
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'


class Tarea(models.Model):
    persona = models.ForeignKey('Persona', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_limite = models.DateField()
    completada = models.BooleanField(default=False)

