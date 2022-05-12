from django.http import HttpResponse
import json

from django.shortcuts import render

# Create your views here.

def applicants_view_json(request):
    return render(request, 'index.html')

def applicants_view_sql(request):
    return render(request, 'SQLDataView.html')

def applicants_view_db(request):
    return render(request, 'dbView.html')