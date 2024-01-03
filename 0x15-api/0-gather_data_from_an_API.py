#!/usr/bin/python3
"""
   Module that access API of user's todo list
"""

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
        employee_name = matching_user['name']
        todo_url = f'{base_url}/todos?userId={employee_ID}'
        todo_response = requests.get(todo_url)
        todo_data = todo_response.json()
        completed = []
        for todo in todo_data:
            if todo['completed']:
                completed.append(todo)
        number_of_complete = len(completed)
        total_number = len(todo_data)
        print("Employee {} is done with tasks({}/{}):".format(
            employee_name, number_of_complete,
            total_number))

        for task in completed:
            print(f"\t {task['title']}")
