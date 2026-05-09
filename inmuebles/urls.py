from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import PropiedadViewSet, PropietarioViewSet

router = DefaultRouter()
router.register(r"propiedades", PropiedadViewSet, basename="propiedad")
router.register(r"propietarios", PropietarioViewSet, basename="propietario")

# Alias opcionales para coincidir con la nomenclatura genérica de la rúbrica.
router.register(r"entidad1", PropiedadViewSet, basename="entidad1")
router.register(r"entidad2", PropietarioViewSet, basename="entidad2")

urlpatterns = [
    path("", include(router.urls)),
]
