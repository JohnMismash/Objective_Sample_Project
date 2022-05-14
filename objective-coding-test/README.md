Coding Test Instructions
========================

The purpose of this test is to determine your ability to learn quickly, analyze
problems, and produce logic to solve these problems. I will also be looking at
code readability and cleanliness.

In this tarball
---------------

You'll find a sample data set in three different forms, for your convenience.
Specifically, data.sqlite3 (sqlite3 database), data.sql (a MySQL database dump),
and data.json (a JSON object).

This test set also includes example output in the form of an HTML page:
index.html.

Problem
-------

Your task is to use the data provided and implement some sort of application
(Ruby on Rails, Django, Laravel, React, node.js, your own custom application,
etc.) to output the data in a format that matches as closely as possible the
HTML structure shown in index.html (the actual HTML, not just how it looks
when rendered in the browser). Your solution should accept any data set like
the one provided, so it must allow any number of skills per person, any number
of jobs, and any number of applicants.

Your solution *must not* use CSS styles
to format the HTML, except for what is already provided in the index.html
example.

Please feel free to ask questions: sam@objectiveinc.com or jonathon@objectiveinc.com.

Additional Info
---------------

The following is a summary of the data provided.

#### Job

* Columns:
  * id: integer
  * name: string (e.g. Web Developer)

#### Applicant

* Columns:
  * id: integer
  * name: string
  * email: string
  * website: string
  * cover_letter: text
  * job_id: integer
* Relationships:
  * has one job
  * has many skills

#### Skill

* Columns:
  * id: integer
  * name: string
  * applicant_id: integer


Developer Notes:
================
Author: John 'Jack' Mismash
Date: 5/10/22
Language: Python
Framework: Django

Project Notes:
- The server is managed through the settings.py file, and has the 'playground' app installed.
- The server-wide URL patterns includes the playground app as part of its path.
- The playground app contains the specific URL patterns that are part of the path as well as the HTTP request handlers.
- The launch profile (launch.json file) includes a port number of 9000 for debugging purposes.
- This project also has configuration for a debugging toolbar that can be found outlined in the Installed Apps and Middleware portion of the settings file.
- Within settings.py, DEBUG must be set to false when in production.
- The SECRET_KEY is unique ot every Django project, and can be changed during development phases.
- 'python manage.py migrate' syncs all local settings with the db.sqlite3 database.
- 'python manage.py createsuperuser' creates a SuperUser to manage all admin settings such as users or groups.
- The request.user parameter can allow the develop to see the admins and users who request the page.
- Template reference is independent of OS, can be referenced within the project.
- Redirecting is possible through a request handler with the redirect() function.

Solution Notes:
- The Jobs and corresponding Applicants have a one to many relationship, where one Job may have multiple Applicants.
- The Applicants and their corresponding Skills have a one to many relationship, where one applicant may have multiple skills, but only one of each skill.
- The data.sqllite database is connected to this project.
  - For reading the data, this project assumes all values are re-written to the database or updated from another source, although I manually upload the same values every time
    with the data from the data.json file for the sake of showing the data is being re-populated every time.
- The data.sql file dump is not correctly connecting to mySQL server. I created a mySQL server and database, dumped the data into it, but I can't seem to figure out how to connect it
  to the applicants_sql app so it will pull data from the correct database.
- There are three urls to follow:
  - home/applicants-JSON: Corresponds to the JSON data being rendered.
  - home/applicants-sqllite: Corresponds to the sqllite3 database.
  - db/applicants-sql: Corresponds to the sql database.
