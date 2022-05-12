from django.urls import path
from . import views


urlpatterns = [
    path('applicants-JSON/', views.applicants_view_json),

    path('applicants-SQL/', views.applicants_view_sql),

    path('applicants-DB/', views.applicants_view_db)

    # __debug__/
    # path('__debug__/', include('debug_toolbar.urls')),
]

