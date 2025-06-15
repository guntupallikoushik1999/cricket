from django.shortcuts import render
from rest_framework.views import APIView, Response
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
    def get_queryset(self):
        queryset = Bowler.objects.all()
        name = self.request.query_params.get('name')
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset
    