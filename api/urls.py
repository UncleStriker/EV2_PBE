from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register('Mascota', views.MascotaViewSet)

urlpatterns = [

    path('',include(router.urls))

]