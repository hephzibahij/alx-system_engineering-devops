#!/usr/bin/python3
"""
   Module that access API of user's todo list
"""
import json
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
        json_data = {str(employee_ID): []}
        for task in todo_data:
            json_data[str(employee_ID)].append({
                "task": task['title'],
                "completed": task['completed'],
                "username": employee_name})
        json_filename = "{}.json".format(employee_ID)
        with open(json_filename, "w") as file:
            json.dump(json_data, file)
