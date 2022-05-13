# Objective - Sample Project:
# Application Configuration

# Author: John 'Jack' Mismash
# Date: 5/10/22from django.apps import AppConfig

from django.apps import AppConfig


class ApplicantsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'applicants'
