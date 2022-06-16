from pyexpat import model
from rest_framework import serializers
from .models import Descripcion


#DESCRIPCION SERIALIZERS

class DescripcionSerializers(serializers.ModelSerializers):

    class Meta:
        model = Descripcion
        fields = ['id', 'descripcion_clima', 'temperatura', 'crear_en']
