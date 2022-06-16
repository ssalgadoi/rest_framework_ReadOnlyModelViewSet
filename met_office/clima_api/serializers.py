

from .models import Descripcion
from rest_framework import serializers


#DESCRIPCION SERIALIZERS

class DescripcionSrializers(serializers.ModelSerializer):

    class Meta:
        model = Descripcion
        fields = '__all__'
