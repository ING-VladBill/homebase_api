from rest_framework import serializers

from .models import Propiedad, Propietario


class PropiedadResumenSerializer(serializers.ModelSerializer):
    """Representación resumida de propiedades asociadas a un propietario."""

    tipo_display = serializers.CharField(source="get_tipo_display", read_only=True)

    class Meta:
        model = Propiedad
        fields = ["id", "direccion", "precio", "tipo", "tipo_display"]


class PropietarioSerializer(serializers.ModelSerializer):
    """Serializa los datos de los propietarios junto con sus propiedades."""

    total_propiedades = serializers.IntegerField(source="propiedades.count", read_only=True)
    propiedades = PropiedadResumenSerializer(many=True, read_only=True)

    class Meta:
        model = Propietario
        fields = [
            "id",
            "nombre",
            "documento_identidad",
            "telefono",
            "email",
            "total_propiedades",
            "propiedades",
            "creado_en",
            "actualizado_en",
        ]
        read_only_fields = [
            "id",
            "total_propiedades",
            "propiedades",
            "creado_en",
            "actualizado_en",
        ]


class PropiedadSerializer(serializers.ModelSerializer):
    """Serializa las propiedades y muestra información asociada del propietario."""

    propietario_nombre = serializers.CharField(source="propietario.nombre", read_only=True)
    propietario_documento = serializers.CharField(source="propietario.documento_identidad", read_only=True)
    tipo_display = serializers.CharField(source="get_tipo_display", read_only=True)

    class Meta:
        model = Propiedad
        fields = [
            "id",
            "direccion",
            "precio",
            "tipo",
            "tipo_display",
            "descripcion",
            "propietario",
            "propietario_nombre",
            "propietario_documento",
            "creado_en",
            "actualizado_en",
        ]
        read_only_fields = [
            "id",
            "tipo_display",
            "propietario_nombre",
            "propietario_documento",
            "creado_en",
            "actualizado_en",
        ]
