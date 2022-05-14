# Objective - Sample Project:
# Admin/Model Configuration

# Author: John 'Jack' Mismash
# Date: 5/10/22

from django.contrib import admin
from .models import Applicant

# Register your models here.

admin.site.register(Applicant)