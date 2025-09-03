from django.shortcuts import get_object_or_404, render
from.models import Persona,Tarea
from.serializers import PersonaSerializer,TareaSerializer
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import generics, status
from django.http import HttpResponse
from django.http import JsonResponse
from django.utils.dateparse import parse_date
from django.db import models


#vistas

#tareas
class TareaListCreate(generics.ListCreateAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer

class TareaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
#_________________________________
class PersonaByDocumentoList(generics.ListAPIView):
    serializer_class = PersonaSerializer

    def get_queryset(self):
        documento = self.request.query_params.get('documento')
        return Persona.objects.filter(documento=documento)
# ------------------ PERSONAS ------------------

# --------- CRUD Personas ------------
class PersonaListCreateView(generics.ListCreateAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer

class PersonaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer

class PersonaPorDocumentoView(generics.RetrieveAPIView):
    serializer_class = PersonaSerializer
    lookup_field = "documento"
    queryset = Persona.objects.all()

# ------------ CRUD Tareas -----------
class TareaListCreateView(generics.ListCreateAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer

class TareaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer

# ----------------- Filtros Tareas -----------------
class TareaByFechaList(generics.ListAPIView):
    serializer_class = TareaSerializer

    def get_queryset(self):
        fecha = self.request.query_params.get('fecha')
        if fecha is None:
            return Tarea.objects.all()  # opcional: retornar todas si no hay fecha
        return Tarea.objects.filter(fecha_limite=fecha)

class TareasPorRangoList(generics.ListAPIView):
    serializer_class = TareaSerializer

    def get_queryset(self):
        fecha_inicio = self.kwargs['fecha_inicio']
        fecha_fin = self.kwargs['fecha_fin']
        return Tarea.objects.filter(fecha_limite__range=[fecha_inicio, fecha_fin])

class TareasPorPersonaList(generics.ListAPIView):
    serializer_class = TareaSerializer

    def get_queryset(self):
        documento = self.kwargs.get('documento')  # solo documento
        try:
            persona = Persona.objects.get(documento=documento)
            return Tarea.objects.filter(persona=persona)
        except Persona.DoesNotExist:
            return Tarea.objects.none()


def hola_mundo(request):
    return JsonResponse({"mensaje": "Hola desde Django API 🚀"})

def home(request):
    return HttpResponse("Hola, Django está funcionando 🚀")



class PersonaList(generics.ListCreateAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer


    def get(self, request):
        personas= Persona.objects.all()
        serializer = PersonaSerializer (personas, many=True)
        if not personas:
            raise NotFound('No se encontraron personas.')
        return Response({'success': True, 'detail': 'Listado de personas.', 'data': serializer.data}, status=status.HTTP_200_0K)


# Crear personas
class CrearPersona(generics.CreateAPIView):
     queryset =Persona.objects.all()
     serializer_class = PersonaSerializer
     def post(self, request):
      serializer = PersonaSerializer (data=request.data)
      serializer. is_valid(raise_exception=True)
      serializer.save
      return Response({'success': True, 'detail': 'Persona creada correctamente.', 'data': serializer.data}, status=status .HTTP_201_CREATED)


#Actualizar personas
class ActualizarPersona (generics.UpdateAPIView):
     queryset = Persona.objects.all
     serializer_class = PersonaSerializer
     def put(self, request, pk):
         persona =get_object_or_404 (Persona, pk=pk)
         email = request.data.get('email', None)
# Verificar si el email ha cambiado
         if email and email != persona.email:
# Verificar si ya existe otra persona con el mismo email
             if Persona.objects.filter(email=email).exclude(pk=pk).exists():
                 return Response({' email': ['Persona with this email already exists.']}, status-status.HTTP_400_BAD_REQUEST)
         serializer = PersonaSerializer (persona, data=request.data)
         serializer. is_valid(raise_exception=True)
         serializer.save()
         return Response({'success': True, 'detail': 'Persona actualizada correctamente.', 'data': serializer.data}, status=status.HTTP_200_OK)
# Buscar persona por documento
class PersonaByDocumento (generics.ListAPIView):
     serializer_class = PersonaSerializer


     def get(self, request, documento):
         persona = Persona.objects. filter (documento=documento) .first()
         if not persona:
             raise NotFound('No se encontró una persona con ese documento.')
         serializer = PersonaSerializer (persona)
         return Response({'success': True, 'detail': 'Persona encontrada.', 'data': serializer.data},status=status.HTTP_200_0K) 