""" URL configuration for the bowlers app.
This module sets up the URL routing for the BowlerViewSet, allowing for CRUD operations on bowler instances.
# It uses Django's DefaultRouter to automatically generate the necessary routes for the BowlerViewSet.
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BowlerViewSet
# This code sets up the URL routing for the BowlerViewSet, allowing for CRUD operations on bowler instances.


router = DefaultRouter()
router.register(r'bowlers', BowlerViewSet)

urlpatterns = [
    path('', include(router.urls)),
#    path('bowlers/', BowlerViewSet.as_view({'get': 'list', 'post': 'create'}), name='bowler-list'),
    #path('bowlers/<str:key>/', BowlerCrud.as_view(), name='bowler-detail'),
]
# This code sets up the URL routing for the BowlerViewSet, allowing for CRUD operations on bowler instances.
