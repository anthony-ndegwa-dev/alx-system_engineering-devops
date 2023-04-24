#!/usr/bin/python3
"""
 Extend your task #0 Python script to export data in the JSON format.

Requirements:

    Records all tasks from all employees
    Format must be: { "USER_ID": [ {"username": "USERNAME", "task":
     "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username":
      "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS},
       ... ], "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE",
       "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task":
       "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}
    File name must be: todo_all_employees.json
"""
import json
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user = '{}users'.format(url)
    res = requests.get(user)
    json_o = res.json()
    d_task = {}
    for user in json_o:
        name = user.get('username')
        userid = user.get('id')
        todos = '{}todos?userId={}'.format(url, userid)
        res = requests.get(todos)
        tasks = res.json()
        l_task = []
        for task in tasks:
            dict_task = {"username": name,
                         "task": task.get('title'),
                         "completed": task.get('completed')}
            l_task.append(dict_task)

        d_task[str(userid)] = l_task
    filename = 'todo_all_employees.json'
    with open(filename, mode='w') as f:
        json.dump(d_task, f)
