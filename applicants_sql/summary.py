# Objective - Sample Project:
# Summary Class

# Author: John 'Jack' Mismash
# Date: 5/10/22

import json
from .models import Job, Applicant, Skill

# This class represents the bundling of data betweent the Jobs, Applicants, and Skills.
# Creates a model object for each Job, Applicant, and Skill that is pushed to the database.
class Summary:
    def __init__(self, jobs, applicants, skills):

       self.jobs_json = jobs
       self.applicants_json = applicants
       self.skills_json = skills

       self.jobs = []
       self.applicants = []
       self.skills = []

       for job in self.jobs_json:
            id_no = job['id']
            name = job['name']

            current = Job(int(id_no), name)
            self.jobs.append(current)

       for applicant in self.applicants_json:
           id_no = applicant['id']
           name = applicant['name']
           email = applicant['email']
           website = applicant['website']
           cover_letter = applicant['cover_letter']
           job_id = applicant['job_id']

           current = Applicant(int(id_no), name, email, website, cover_letter, job_id)
           self.applicants.append(current)

       for skill in self.skills_json:
            id_no = skill['id']
            name = skill['name']
            applicant_id = skill['applicant_id']

            current = Skill(int(id_no), name, applicant_id)
            self.skills.append(current)


    @staticmethod
    def from_json(json_string):
        json_dict = json.loads(json_string)
        # print(json_dict)
        return Summary(json_dict["jobs"], json_dict["applicants"], json_dict["skills"])

    # Debugging
    def __ref__(self):

        for applicant in self.applicants:
            print(f'Applicant: {applicant.id}')
            print(applicant.name)
            print(applicant.email)
            print(applicant.website)
            print(applicant.cover_letter)
            print(f'Job ID: {applicant.job_id}')
            print('')

        for job in self.jobs:
            print(f'Job: {job.id}')
            print(job.name)
            print('')

        for skill in self.skills:
            print(f'Skill: {skill.id}')
            print(f'{skill.name}')
            print(f'Applicant ID: {skill.applicant_id}')
            print('')