from django.http import HttpResponse
from django.shortcuts import render
import json

class Summary:
    def __init__(self, applicants, jobs, skills) -> None:
        self.applicants = applicants
        self.jobs = jobs
        self.skills = skills
    
    @staticmethod
    def from_JSON(json_string):
        json_dict = json.loads(json_string)
        return Summary(**json_dict)

    def to_HTML(self):
        return f'Job Applicants: {self.applicants}'


# Create your views here.

def applicants_view_json(request):
    file = open('data.json', "r")
    json_string = file.read()

    summary = Summary.from_JSON(json_string)
    file = open('JSONView.html', "w")
    file.write(summary.to_HTML())
    file.close()

    return render(request, 'JSONView.html')

def applicants_view_sql(request):
    return render(request, 'SQLDataView.html')

def applicants_view_db(request):
    return render(request, 'dbView.html')

def applicants_view_ref(request):
    return render(request, 'index.html')

