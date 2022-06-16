from django.urls import path, include
from clima_api import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('descripcion', views.DescripcionViewSet)

urlpatterns = [
    path('',include(router))

]