from django.shortcuts import render
from rest_framework import viewsets
from .serializer import MascotaSerializer
from .models import Mascota

# Create your views here.


class MascotaViewSet(viewsets.ModelViewSet):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer