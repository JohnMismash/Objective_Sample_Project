# Objective - Sample Project:
# Model Configuration

# Author: John 'Jack' Mismash
# Date: 5/10/22


from ast import iter_child_nodes
from asyncio.base_subprocess import WriteSubprocessPipeProto
from asyncio.windows_events import NULL
import email
from unicodedata import name
from django.db import models

# Create your models here.

class applicant(models.Model):
    id_no = models.IntegerField(default = NULL)
    name = models.TextField(default = "")
    email = models.TextField(default = "")
    website = models.TextField(default = "")
    cover_letter = models.TextField(default = "")
    job_id = models.IntegerField(default = NULL)

    def __str__(self):
        return self.name

class job(models.Model):
    id_no = models.IntegerField()
    name = models.TextField()

    def __str__(self):
        return self.name

class skill():
    id_no = models.IntegerField()
    name = models.TextField()
    applicant_id = models.IntegerField()

    def __str__(self):
        return self.name

    