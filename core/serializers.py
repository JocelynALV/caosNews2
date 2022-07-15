#este se encarga de transformar datos a Json o desde Json se encarga de guardar, modificar, listar y eliminar datos

from .models import Noticia
from rest_framework import serializers

class NoticiaSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Noticia
        fields = '__all__'




