# Artist Link Web App

## Brief
As a final individual project on the QA DevOps Boot Camp we were asked to write a web application to achieve the following objectives:
"
* To create a multi-tier web application that demonstrates CRUD functionality.
* To utilise containers to host and deploy your application.
* To create a continuous integration (CI)/continuous deployment (CD) pipeline that will automatically test, build and deploy your application.
"

This will showcase all the topics we have learned over a nine week period.

### Additional Requirements
The components required to demonstrate the objective were as follows:

* A Jira / Trello board for planning
* A MySQL Database for Azure, consisting of at least two tables that model a relationship
* A Flask driven frontend service to host the web pages that will implement CRUD capability to retrieve information from this database
* Automated unit testing using pytest in a CI/CD pipeline, implemented using Jenkins inside a Docker container
* Use of git and GitHub within Jenkins to orchestrate development to the Azure virtual machine

### Implementation
To achieve the requirements I initially set out to produce a website which would allow fledgling musicians to book gigs online with venues (pubs and clubs primarily).
The venues would post their details on a simple form, specifying capacity, changing room facilities, renumeration and the like, and the band would complete their own form specifying music genre, number of band members, rider requirements etc.
After a reviewing this specification I came to the conclusion that this would require a many-to-many relationship and may be a bit ambitious for a first project, especially given the time constraint.
Eventually I settled on an agent to band relationship as this would pare it down to a the 'one agent has many bands, a band has only one agent' scenario, modelling a simpler one to many relationship.

Agent - Band tables
* Band CREATEs an account:
   * Name of band
   * Genre of music (pulldown from list)
   * Number of people in band
   * Contact email

* Agent CREATES an account:
   * Name of agent
   * Number of bands on roster (UPDATE capability)
   * Percentage cut (5%, 10%, 20%, negotiable)

DELETE capability would be shown when the band decides on an agent, their account would be deleted so it wouldn't appear in the pool of talent.

When an agent wants to see the pool of talent or vice versa, the app would display a list of available agents/bands, requiring READing from the database.

The ERD can be found here: 

(JPEG)  https://1drv.ms/u/s!Aq2hJel0GwxWpCG6pbWS-pBpEUQM?e=8Xdjoj

(PDF)   https://1drv.ms/b/s!Aq2hJel0GwxWpCIA6VLs0hl0AQSp?e=aOc4Kz

## User stories
* As a band we want to add our details to available bands list so that we are visible to agents (CREATE)
* As a band we want to review our entry so that our information is correct (READ)
* As a band we want to be able to change details (band members/name) so that is information is always accurrate (UPDATE)
* As an band/agent we want the band entry deleted when signed so that the band is no longer available (DELETE)
* As an agent I want to add my details to available agents list so that I we are visible to bands (CREATE)
* As a agent I want to review/change my entry so that our information is correct (UPDATE)

## Risk assessment
* Loss of ssh keys