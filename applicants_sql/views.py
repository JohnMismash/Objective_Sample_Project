from django.shortcuts import render
from .models import Job, Applicant, Skill
from applicants_sql.summary import Summary
from bs4 import BeautifulSoup as bs

# Create your views here.

def applicants_view_sql(request):
    with open('data.json', "r") as json_file:
        applicant_summary = Summary.from_json(json_file.read())

        # Data read from data.json file.
        jobs = applicant_summary.jobs
        applicants = applicant_summary.applicants
        skills = applicant_summary.skills

        delete_from_db()

        # Write data into the db.
        write_to_db(jobs, applicants, skills)

        # Data read back from db.
        jobs, applicants, skills = read_from_db()
        
        filename = 'templates/SQLView.html'

        create_html(jobs, applicants, skills, filename)


    return render(request, 'sqlView.html')

# Deletes all data from the db to repopulate all values from the file (assuming the file is constantly changing, or writing to the db is based on a different source).
def delete_from_db():
    jobs = Job.objects.all()
    applicants = Applicant.objects.all()
    skills = Skill.objects.all()

    for job in jobs:
        temp = Job.objects.get(id=job.id)
        temp.delete()

    for applicant in applicants:
        temp = Applicant.objects.get(id=applicant.id)
        temp.delete()

    for skill in skills:
        temp = Skill.objects.get(id=skill.id)
        temp.delete()


def write_to_db(jobs, applicants, skills):
    for job in jobs:
        entry = Job(id=job.id, name=job.name)
        entry.save()

    for applicant in applicants:
        entry = Applicant(id=applicant.id, name=applicant.name, email=applicant.email, website=applicant.website, cover_letter=applicant.cover_letter, job_id=applicant.job_id)
        entry.save()

    for skill in skills:
        entry = Skill(id=skill.id, name=skill.name, applicant_id=skill.applicant_id)
        entry.save()

    return

def read_from_db():

    jobs = Job.objects.all()
    applicants = Applicant.objects.all()
    skills = Skill.objects.all()

    return jobs, applicants, skills


    # Method for creating the html of each request type.
# Note: This HTML could have simply been done with templates and utilizing for loopps/conditions within the HTML doc itself (see base.html).
def create_html(jobs, applicants, skills, filename):

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
    file = open(filename, "w")
    file.write(output)
    file.close

    return html