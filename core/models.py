from distutils.command.upload import upload
from unittest.util import _MAX_LENGTH
from django.db import models
import cx_Oracle
cx_Oracle.init_oracle_client(lib_dir=r"C:\oracle\instantclient_21_6")
import os 

# Create your models here.

class Noticia(models.Model):
    idNoticia =models.IntegerField(primary_key=True, verbose_name='Id de la noticia')
    titulo =models.CharField(max_length=50, verbose_name='Titolo de la noticia')
    encabezado_noticia =models.CharField(max_length=50, verbose_name='Encabezado de la noticia')
    cuerpo_noticia =models.CharField(max_length=250, verbose_name='Cuerpo de la noticia')
    foto_noticia =models.ImageField(upload_to="images/", null=True, blank=True)
    fecha =models.DateField()

    def __str__(self):
        return self.titulo


class Periodista(models.Model):
    rut =models.CharField(primary_key=True, max_length=10, verbose_name='Rut de periodista')
    nombre =models.CharField(max_length=250, verbose_name='Nombre del periodista')
    correo =models.EmailField(max_length=200, verbose_name='Correo electronico de periodista')
    foto_periodista =models.ImageField(upload_to="images/", null=True, blank=True)


    def __str__(self):
        return self.nombre