import requests 
import json
import time


page = 1
job_data = []

response = requests.get('http://212.159.75.17:8000/jobs?page={0}'.format(page), auth=('admin', 'media101')).json()
numberOfJobs = response['count']
numberOfPages = round(numberOfJobs / 10, 0)

while page <= numberOfPages:

	print("Getting jobs from page: {0}".format(page))
	response = requests.get('http://212.159.75.17:8000/jobs?page={0}'.format(page), auth=('admin', 'media101')).json()

	job_data.extend(response['jobs'])


	page += 1

print("Jobs Number: {0}".format(len(job_data)))


with open('jobs_data.json', 'w') as outfile:
    json.dump(job_data, outfile, indent=4)