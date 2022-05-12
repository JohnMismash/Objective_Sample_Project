from asyncio.base_subprocess import WriteSubprocessPipeProto
import email
from django.db import models

# Create your models here.

class applicant(models.Model):
    id_no = models.IntegerField()
    name = models.TextField()
    skills = models.TextField(default='Skills')

