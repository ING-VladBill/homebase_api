from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import PropiedadViewSet, PropietarioViewSet

router = DefaultRouter()
router.register(r"propiedades", PropiedadViewSet, basename="propiedad")
router.register(r"propietarios", PropietarioViewSet, basename="propietario")

urlpatterns = [
    path("", include(router.urls)),
]
