# Generated by Django 4.0.4 on 2022-05-12 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicants', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='id_no',
            field=models.IntegerField(),
        ),
    ]