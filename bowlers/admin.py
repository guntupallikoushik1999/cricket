"""
Admin configuration for the Bowler model.
This module registers the Bowler model with the Django admin site, allowing it to be managed through the admin interface.
"""
from django.contrib import admin
from .models import Bowler
# Register your models here.
admin.site.register([
    Bowler,
])
# Register your models here, e.g., admin.site.register(Bowler)
