from .models import Querys
from rest_framework import serializers
from django.contrib.auth.models import User


class ConsultaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Querys
        fields = ['url', 'consulta', 'respuesta', 'date']
        
