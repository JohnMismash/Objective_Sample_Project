# Objective - Sample Project:
# applicants URL Configuration

# Author: John 'Jack' Mismash
# Date: 5/10/22

from django.urls import include, path
from . import views

urlpatterns = [
    path('applicants-JSON/', views.applicants_view_json),
    path('applicants-sqllite/', views.applicants_view_sqllite3),
    path('applicants-DB/', views.applicants_view_sql),
    path('applicants-ref/', views.applicants_view_ref),
]

