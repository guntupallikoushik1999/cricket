from django.shortcuts import render
from rest_framework.views import APIView, Response
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Max
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
        if age := self.request.query_params.get('age'): # Filter by age in one liner with if statement check name above for more info
            queryset = queryset.filter(age=age)
        if country := self.request.query_params.get('country'):
            queryset = queryset.filter(country__icontains=country)
        if wickets_taken := self.request.query_params.get('wickets_taken'):
            queryset = queryset.filter(wickets_taken=wickets_taken)
        if bowling_average := self.request.query_params.get('bowling_average'):
            queryset = queryset.filter(bowling_average=bowling_average)
        if bowling_strikerate := self.request.query_params.get('bowling_strikerate'):
            queryset = queryset.filter(bowling_strikerate=bowling_strikerate)
        if economy_rate := self.request.query_params.get('economy_rate'):
            queryset = queryset.filter(economy_rate=economy_rate)
        if self.request.query_params.get('sort_by'):
            sort_by = self.request.query_params.get('sort_by')
            queryset = queryset.order_by(sort_by)
        """ 
        order_by
        Default DRF sort is ascending order.
        ?sort_by=name → ascending
        ?sort_by=-name → descending"""
        return queryset
    @action(detail=False, methods=['get'], url_path='highest_wicket_taker')
    #Add a custom GET endpoint called /highest_wicket_taker/ to the BowlerViewSet.
    # This endpoint will return the bowler(s) with the highest number of wickets taken.
    def highest_wicket_taker(self, request):
        max_wickets = Bowler.objects.aggregate(Max('wickets_taken'))['wickets_taken__max']
        top_bowlers = Bowler.objects.filter(wickets_taken=max_wickets)
        #above line gets the bowler(s) with the highest number of wickets taken by using aggregate function in Django ORM 
        #top_bowlers = Bowler.objects.raw('SELECT * FROM bowlers_bowler WHERE wickets_taken > 300')
        #above line is an example of raw SQL query to get bowlers with more than 300 wickets we can write any SQL query here
        serializer = self.get_serializer(top_bowlers, many=True)
        return Response(serializer.data)
        #return Response(top_bowlers.values('name', 'wickets_taken', 'country'))

    