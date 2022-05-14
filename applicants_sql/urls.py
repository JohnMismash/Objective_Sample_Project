# Objective - Sample Project:
# applicants_sql URL Configuration

# Author: John 'Jack' Mismash
# Date: 5/10/22


from django.urls import path
from . import views

urlpatterns = [
    path('applicants-sql/', views.applicants_view_sql),
]