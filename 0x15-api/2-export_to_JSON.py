#!/usr/bin/python3
"""
 Extend your task #0 Python script to export data in the JSON format.

Requirements:

    Records all tasks that are owned by this employee
    Format must be: { "USER_ID": [{"task": "TASK_TITLE", "completed":
     TASK_COMPLETED_STATUS, "username": "USERNAME"}, {"task": "TASK_TITLE",
     "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}
    File name must be: USER_ID.json
"""
import json
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    userid = sys.argv[1]
    user = '{}users/{}'.format(url, userid)
    res = requests.get(user)
    json_o = res.json()
    name = json_o.get('username')

    todos = '{}todos?userId={}'.format(url, userid)
    res = requests.get(todos)
    tasks = res.json()
    l_task = []
    for task in tasks:
        dict_task = {"task": task.get('title'),
                     "completed": task.get('completed'),
                     "username": name}
        l_task.append(dict_task)

    d_task = {str(userid): l_task}
    filename = '{}.json'.format(userid)
    with open(filename, mode='w') as f:
        json.dump(d_task, f)
