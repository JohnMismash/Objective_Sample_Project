# Objective - Sample Project:
# View Configuration

# Author: John 'Jack' Mismash
# Date: 5/10/22

from django.shortcuts import render
from applicants.summary import Summary
from bs4 import BeautifulSoup as bs

# Create your views here.

def applicants_view_json(request):
    with open('data.json', "r") as json_file:
        applicant_summary = Summary.from_json(json_file.read())
        # applicant_summary.__ref__()

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

# Method for creating the html of each request type.
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
                                </thead>
                                <tbody>"""

    counter = 0

    for job in jobs:

        job_id = job.id
        current_job_applicants = []
        
        for applicant in applicants:
            if (applicant.job_id == job_id):
                current_job_applicants.append(applicant)
                    

        skill_counter = 0

        for skill in skills:  
            if (skill.applicant_id == applicant.id):
                skill_counter += 1

        html = html + "<tr>"
        html = html + "<td rowspan=\"" + str(skill_counter) + "\">" + job.name + "</td>"

        skill_counter = 0

        for applicant in current_job_applicants:
            counter += 1
            current_applicant_skills = []
            
            print(applicant.name)

            applicant_skill_counter = 0

            for skill in skills:  
                if (skill.applicant_id == applicant.id):
                    current_applicant_skills.append(skill)
                    print(skill.name)
                    skill_counter += 1
                    applicant_skill_counter += 1

            if (counter is not 1):
                html = html + "<tr>"

            html = html + "<td rowspan=\"" + str(applicant_skill_counter) + "\">" + applicant.name + "</td>"
            html = html + "<td rowspan=\"" + str(applicant_skill_counter) + "\">" + applicant.email + "</td>"
            html = html + "<td rowspan=\"" + str(applicant_skill_counter) + "\">" + applicant.website + "</td>"
            html = html + "<td>" + str(current_applicant_skills[0].name) + "</td>"
            html = html + "<td rowspan=\"" + str(applicant_skill_counter) + "\">" + applicant.cover_letter + "</td>"

            html = html + "</tr>"

            for skill_no in range(applicant_skill_counter):
                if (skill_no is not 1):
                    html = html + "<tr>"
                    html = html + "<td>" + str(current_applicant_skills[skill_no].name) + "</td>"
                    html = html + "</tr>"

    html = html + "</tr>"

    html = html + """     </tbody>
                        </table>
                       </div>
                      </body>
                    </html>"""

    output = bs(html, 'html.parser').prettify()
    file = open('templates/test.html', "w")
    file.write(output)
    file.close

  


