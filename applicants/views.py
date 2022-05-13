# Objective - Sample Project:
# View Configuration

# Author: John 'Jack' Mismash
# Date: 5/10/22

from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import render
from applicants.summary import Summary
import templates


# Create your views here.

def applicants_view_json(request):
    with open('data.json', "r") as json_file:
        applicant_summary = Summary.from_json(json_file.read())
        applicant_summary.__ref__()

    return render(request, 'JSONView.html')

def applicants_view_sql(request):
    return render(request, 'SQLDataView.html')

def applicants_view_db(request):
    return render(request, 'dbView.html')

def applicants_view_ref(request):
    return render(request, 'index.html')

