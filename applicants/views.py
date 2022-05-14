# Objective - Sample Project:
# View Configuration

# Author: John 'Jack' Mismash
# Date: 5/10/22

from django.shortcuts import render
from applicants.summary import Summary
from bs4 import BeautifulSoup as bs

# Create your views here.

# Renders the html produced from the .json file given.
def applicants_view_json(request):
    with open('data.json', "r") as json_file:
        applicant_summary = Summary.from_json(json_file.read())
    
        jobs = applicant_summary.jobs
        applicants = applicant_summary.applicants
        skills = applicant_summary.skills

        create_html(jobs, applicants, skills)

    return render(request, 'JSONView.html')

# Renders the html produced from the sql dump file.
def applicants_view_sql(request):


    return render(request, 'SQLDataView.html')

def applicants_view_db(request):
    return render(request, 'dbView.html')

# Reference rendering of the provided index.html file.
def applicants_view_ref(request):
    return render(request, 'index.html')

# Method for creating the html of each request type.
def create_html(jobs, applicants, skills):

    # Given CSS styled HTML for basic layout properties.
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

    # Counts the total number of jobs.
    job_counter = 0

    for job in jobs:
        job_counter += 1
        job_id = job.id
        current_job_applicants = []
        
        for applicant in applicants:
            if (applicant.job_id == job_id):
                current_job_applicants.append(applicant)
                    
        skill_counter = 0

        # Finds the number of skills total for the current job and its specific applicants.
        for applicant in current_job_applicants:
            for skill in skills:
                  
                if (skill.applicant_id == applicant.id):
                    skill_counter += 1

        # Build basic Job HTML
        html = html + "<tr>"
        html = html + "<td rowspan=\"" + str(skill_counter) + "\">" + job.name + "</td>"
        job_done = False

        for applicant in current_job_applicants:
            applicant_skill_counter = 0
            current_applicant_skills = []

            # Finds the number of skills for the current applicant.
            for skill in skills:  
                if (skill.applicant_id == applicant.id):
                    current_applicant_skills.append(skill)
                    applicant_skill_counter += 1

            # Does not add a <tr> if the job was just listed in the HTML.
            if (job_done):
                html = html + "<tr>"
                
            job_done = True

            # Build basic applicant HTML
            html = html + "<td rowspan=\"" + str(applicant_skill_counter) + "\">" + applicant.name + "</td>"
            html = html + "<td rowspan=\"" + str(applicant_skill_counter) + "\">" + applicant.email + "</td>"
            html = html + "<td rowspan=\"" + str(applicant_skill_counter) + "\">" + applicant.website + "</td>"
            html = html + "<td>" + str(current_applicant_skills[0].name) + "</td>"
            html = html + "<td rowspan=\"" + str(applicant_skill_counter) + "\">" + applicant.cover_letter + "</td>"

            html = html + "</tr>"

            # Build basic skill HTML
            if (applicant_skill_counter != 1):
                for skill_no in range(applicant_skill_counter):
                    if (skill_no != 0):
                        html = html + "<tr>"
                        html = html + "<td>" + str(current_applicant_skills[skill_no].name) + "</td>"
                        html = html + "</tr>"
    
    # Build remaining closing HTML
    html = html + """     </tbody>
                        </table>
                       </div>
                      </body>
                    </html>"""

    # Formats the HTML and writes to a new file.
    output = bs(html, 'html.parser').prettify()
    file = open('templates/JSONView.html', "w")
    file.write(output)
    file.close

  


