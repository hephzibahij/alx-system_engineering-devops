#!/usr/bin/python3

"""
   Module that gets a response of all users
   and load into a json file
"""

import json
import requests

base_url = 'https://jsonplaceholder.typicode.com'
users_url = f'{base_url}/users'
users_response = requests.get(users_url)
users_data = users_response.json()

todo_url = f'{base_url}/todos'
todo_response = requests.get(todo_url)
todo_data = todo_response.json()

json_data = {}

for user in users_data:
    user_id = str(user['id'])
    username = user['username']
    user_tasks = []

    for task in todo_data:
        if task['userId'] == user['id']:
            user_tasks.append({
                'username': username,
                'task': task['title'],
                'completed': task['completed']
            })

    json_data[user_id] = user_tasks  # Updated to assign tasks to each user

json_filename = 'todo_all_employees.json'
with open(json_filename, 'w') as json_file:
    json.dump(json_data, json_file)
