from rest_framework import filters, viewsets

from .models import Propiedad, Propietario
from .serializers import PropiedadSerializer, PropietarioSerializer


class PropietarioViewSet(viewsets.ModelViewSet):
    """CRUD completo para propietarios."""

    queryset = Propietario.objects.all()
    serializer_class = PropietarioSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["nombre", "documento_identidad"]
    ordering_fields = ["nombre", "documento_identidad", "creado_en"]


class PropiedadViewSet(viewsets.ModelViewSet):
    """CRUD completo para propiedades con búsqueda por dirección, tipo y propietario."""

    queryset = Propiedad.objects.select_related("propietario").all()
    serializer_class = PropiedadSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["direccion", "tipo", "descripcion", "propietario__nombre"]
    ordering_fields = ["direccion", "precio", "tipo", "creado_en"]
