from django.shortcuts import render

from .models import Querys
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ConsultaSerializer

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from .inteligencia_art import gpt3



class QuerysViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite realizar consultas a una IA
    """
    queryset = Querys.objects.all()
    serializer_class = ConsultaSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def create(self, request):
    
        if request.data.get('consulta') == '':
            serializer = self.get_serializer(data=request.data)
            response = {}
            response['succes'] = False
            response['message'] = "Campo en blanco"
            response['status'] = status.HTTP_404_NOT_FOUND
            return Response(response)
        else:
            respuesta_a = gpt3(request.data.get('consulta'))
            
            serializer = self.get_serializer(data=request.data)
            response = {}
            response['succes'] = True
            response['message'] = "Registro guardado exitosamente"
            response['status'] = status.HTTP_201_CREATED
            response['response'] = respuesta_a
            
            Querys.objects.create(consulta=request.data.get('consulta'), respuesta=respuesta_a)
            
            return Response(response)

