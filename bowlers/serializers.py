"""
Serializers for the Bowler model.
This module defines the serializer for the Bowler model, which is used to convert model instances to JSON format and vice versa.

This serializer will be used in the views to handle the serialization and deserialization of Bowler instances.
"""
from rest_framework import serializers
from .models import Bowler

class BowlerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bowler
        fields = '__all__'  # or specify fields like ['name', 'age', 'country', ...]