
from rest_framework import serializers
from .models import Descripcion


#DESCRIPCION SERIALIZERS

class DescripcionSrializers(serializers.ModelSerializer):

    class Meta:
        model = Descripcion
        fields = ['id', 'descripcion_clima', 'temperatura', 'crear_en']
