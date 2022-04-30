import json
import csv
from datetime import datetime

with open('Flask.json') as file:
    repos = json.loads(file.read())
    with open('flask_repo.csv', 'w') as table:
        headers = ['Name', 'Link', 'Created at', 'Stars']
        writer = csv.writer(table)
        writer.writerow(headers)
        for repo in repos:
            date = datetime.fromisoformat(repo['created'])
            link = 'https://github.com/' + repo['full_name']
            row = [repo['repo_name'], link, date, repo['stars']]
            writer.writerow(row)

