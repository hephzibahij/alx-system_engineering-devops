#!/usr/bin/python3
"""
   Module that connects to an api and save the
   data into a csv file
"""
import csv
import requests
import sys

if __name__ == "__main__":
    employee_ID = int(sys.argv[1])

    base_url = 'https://jsonplaceholder.typicode.com'
    users_url = '{}/users'.format(base_url)
    users_response = requests.get(users_url)
    users_data = users_response.json()

    matching_user = None
    for employee in users_data:
        if employee['id'] == employee_ID:
            matching_user = employee
            break
    if matching_user:
        employee_name = matching_user['username']
        todo_url = f'{base_url}/todos?userId={employee_ID}'
        todo_response = requests.get(todo_url)
        todo_data = todo_response.json()

        completed_tasks = []
        for todo in todo_data:
            if todo['completed']:
                completed_tasks.append(todo)
    filename = f'{employee_ID}.csv'

    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        for task in todo_data:
            csvwriter.writerow([employee_ID, employee_name,
                                str(task['completed']), task['title']])
