# Objective - Sample Project:
# applicants URL Configuration

# Author: John 'Jack' Mismash
# Date: 5/10/22

from django.urls import path
from . import views as applicantsv
from applicants_sql import views as dbv


urlpatterns = [
    path('applicants-JSON/', applicantsv.applicants_view_json),
    path('applicants-sqllite/', applicantsv.applicants_view_sqllite3),
    path('applicants-DB/', dbv.applicants_view_sql),
    path('applicants-ref/', applicantsv.applicants_view_ref),
]

