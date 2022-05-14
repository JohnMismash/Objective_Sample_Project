# Objective - Sample Project:
# Model Configuration

# Author: John 'Jack' Mismash
# Date: 5/10/22


from asyncio.base_subprocess import WriteSubprocessPipeProto
from asyncio.windows_events import NULL
from unicodedata import name
from django.db import models

# Create your models here.

class Applicant(models.Model):
    id = models.IntegerField(primary_key=True, default=0)
    name = models.TextField(default = "")
    email = models.TextField(default = "")
    website = models.TextField(default = "")
    cover_letter = models.TextField(default ="")
    job_id = models.IntegerField(default = NULL)

    def __str__(self):
        return self.name

class Job(models.Model):
    id = models.IntegerField(primary_key=True, default=0)
    name = models.TextField()

    def __str__(self):
        return self.name

class Skill(models.Model):
    id = models.IntegerField(primary_key=True, default=0)
    name = models.TextField()
    applicant_id = models.IntegerField()

    def __str__(self):
        return self.name

    