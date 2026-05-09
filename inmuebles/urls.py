from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import PropiedadViewSet, PropietarioViewSet

router = DefaultRouter()
router.register(r"propiedades", PropiedadViewSet, basename="propiedad")
router.register(r"propietarios", PropietarioViewSet, basename="propietario")

propiedad_list = PropiedadViewSet.as_view({"get": "list", "post": "create"})
propiedad_detail = PropiedadViewSet.as_view(
    {"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"}
)
propietario_list = PropietarioViewSet.as_view({"get": "list", "post": "create"})
propietario_detail = PropietarioViewSet.as_view(
    {"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"}
)

urlpatterns = [
    path("", include(router.urls)),
    path("entidad1/", propiedad_list, name="entidad1-list"),
    path("entidad1/<int:pk>/", propiedad_detail, name="entidad1-detail"),
    path("entidad2/", propietario_list, name="entidad2-list"),
    path("entidad2/<int:pk>/", propietario_detail, name="entidad2-detail"),
]
