from django.urls import include, path
from . import views


urlpatterns = [
    path('applicants-JSON/', views.applicants_view_json),
    path('applicants-SQL/', views.applicants_view_sql),
    path('applicants-DB/', views.applicants_view_db),
    path('applicants-ref/', views.applicants_view_ref),
]

