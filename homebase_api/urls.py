from django.urls import include, path

urlpatterns = [
    path("api/", include("inmuebles.urls")),
    path("", include("inmuebles.urls")),
]
