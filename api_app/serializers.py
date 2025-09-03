from rest_framework import serializers
from.models import Persona, Tarea 

class PersonaSerializer(serializers.ModelSerializer):
     class Meta:
      model=Persona 
      fields ='__all__'
      #____________________

class TareaSerializer(serializers.ModelSerializer):
 class Meta:
  model = Tarea
  fields='__all__'

