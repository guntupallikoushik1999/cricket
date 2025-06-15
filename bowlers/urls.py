from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BowlerViewSet

router = DefaultRouter()
router.register(r'bowlers', BowlerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
# This code sets up the URL routing for the BowlerViewSet, allowing for CRUD operations on bowler instances.
