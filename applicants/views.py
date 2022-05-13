# Objective - Sample Project:
# View Configuration

# Author: John 'Jack' Mismash
# Date: 5/10/22

from ctypes import sizeof
from itertools import count
from django.http import HttpResponse
from django.shortcuts import render
from applicants.summary import Summary
import string

# Create your views here.

def applicants_view_json(request):
    with open('data.json', "r") as json_file:
        applicant_summary = Summary.from_json(json_file.read())
        applicant_summary.__ref__()

        jobs = applicant_summary.jobs
        applicants = applicant_summary.applicants
        skills = applicant_summary.skills

        create_html(jobs, applicants, skills)

    return render(request, 'test.html') # render(request, 'JSONView.html', {'jobs': jobs, 'applicants': applicants, 'skills': skills})

def applicants_view_sql(request):
    return render(request, 'SQLDataView.html')

def applicants_view_db(request):
    return render(request, 'dbView.html')

def applicants_view_ref(request):
    return render(request, 'index.html')

def create_html(jobs, applicants, skills):

    html = """<!DOCTYPE html>
                    <html>
                    <head>
                        <title>Job Applicants Report</title>
                        <link rel="stylesheet" type="text/css" href="http://yui.yahooapis.com/3.9.1/build/cssreset/cssreset-min.css">
                        <link rel="stylesheet" type="text/css" href="http://yui.yahooapis.com/3.9.1/build/cssbase/cssbase-min.css">
                        <style type="text/css">
                        #page {
                            width: 1200px;
                            margin: 30px auto;
                        }
                        .job-applicants {
                            width: 100%;
                        }
                        .job-name {
                            text-align: center;
                        }
                        .applicant-name {
                            width: 150px;
                        }
                        </style>
                    </head>
                    <body>
                        <div id="page">
                        <table>
                            <thead>
                            <tr>
                                <th>Job</th>
                                <th>Applicant Name</th>
                                <th>Email Address</th>
                                <th>Website</th>
                                <th>Skills</th>
                                <th>Cover Letter Paragraph</th>
                            </tr>
                            </thead>"""

    job_counter = len(jobs)
    applicant_counter = 0


    skill_counter = len(skills)
    counter = 0

    for job in jobs:
        counter += 1
        
        for applicant in applicants:
            if (applicant.job_id == counter):
                applicant_counter += 1

        
        html = html + "<tr>"
    
        html = html + "<tr>"
        html = html + "<td rowspan= " + str(applicant_counter) + ">" + job.name + "</td>"
        
        for applicant in applicants:
            if (applicant.job_id == counter):
                html = html + "<td>" + applicant.name + "</td>"

        # html = html + "<td>" + skill.name + "</td>"
        html = html + "</tr>"
        html = html + "</tr>"
    html = html + """ </table>
                        </div>
                      </body>
                    </html> """

    file = open('templates/test.html', "w")
    file.write(html)
    file.close

