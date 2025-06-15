from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Bowler
from .serializers import BowlerSerializer
class BowlerViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing bowler instances.
    """
    queryset = Bowler.objects.all()
    serializer_class = BowlerSerializer
    # You can add additional methods or override existing ones if needed