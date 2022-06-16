from rest_framework import viewsets
from .serializers import DescripcionSerializers
from .models import Descripcion


class DescripcionViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Descripcion.objects.all()
    serializer_class = DescripcionSerializers