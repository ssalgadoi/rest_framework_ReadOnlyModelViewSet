from django.urls import path, include
from .views import DescripcionViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('clima', DescripcionViewSet)

urlpatterns = [
    path('api/',include(router.urls))

]