from rest_framework import serializers
from .models import Bowler

class BowlerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bowler
        fields = '__all__'  # or specify fields like ['name', 'age', 'country', ...]