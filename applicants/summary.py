# Objective - Sample Project:
# Summary, Applicant, Job, and Skill Classes

# Author: John 'Jack' Mismash
# Date: 5/10/22

import json

class Summary:
    def __init__(self, summary):
       self.applicants_json = summary['applicants']
       self.jobs_json = summary['jobs']
       self.skills_json = summary['skills']

       self.applicants = []
       self.jobs = []
       self.skills = []

       for job in self.jobs_json:
            id = job['id']
            name = job['name']

            current = Job(id, name)
            self.jobs.append(current)

       for skill in self.skills_json:
            id = skill['id']
            name = skill['name']
            applicant_id = skill['applicant_id']

            current = Skills(id, name, applicant_id)
            self.skills.append(current)

       for applicant in self.applicants_json:
           id = applicant['id']
           name = applicant['name']
           email = applicant['email']
           website = applicant['website']
           cover_letter = applicant['cover_letter']
           job_id = applicant['job_id']

           current = Applicant(id, name, email, website, cover_letter, job_id)
           self.applicants.append(current)

    @staticmethod
    def from_json(json_string):
        json_dict = json.loads(json_string)
        # print(json_dict)
        return Summary(json_dict)

    # Debugging
    def __ref__(self):
        print('')

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
            print(skill.name)
            print(f'Applicant ID: {skill.applicant_id}')
            print('')


class Applicant:
    def __init__(self, id, name, email, website, cover_letter, job_id):
        self.id = id
        self.name = name
        self.email = email
        self.website = website
        self.cover_letter = cover_letter
        self.job_id = job_id

class Job:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Skills:
    def __init__(self, id, name, applicant_id):
        self.id = id
        self.name = name
        self.applicant_id = applicant_id