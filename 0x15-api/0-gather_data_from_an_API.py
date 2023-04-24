#!/usr/bin/python3
"""
 Python script that, using https://jsonplaceholder.typicode.com/ REST API,
  for a given employee ID, returns information about his TODO list progress.

Requirements:

    You must use urllib or requests module
    The script must accept an integer as a parameter, which is the employee ID
    The script must display on the standard output the employee
     TODO list progress in this exact format:
        First line: Employee EMPLOYEE_NAME is done with tasks
         (NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
            EMPLOYEE_NAME: name of the employee
            NUMBER_OF_DONE_TASKS: number of completed tasks
            TOTAL_NUMBER_OF_TASKS: total number of tasks, which is the sum of
             completed and non-completed tasks
        Second and N next lines display the title of completed tasks:
         TASK_TITLE (with 1 tabulation and 1 space before the TASK_TITLE)
"""
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    user = '{}users/{}'.format(url, sys.argv[1])
    res = requests.get(user)
    json_o = res.json()
    print("Employee {} is done with tasks".format(json_o.get('name')), end="")

    todos = '{}todos?userId={}'.format(url, sys.argv[1])
    res = requests.get(todos)
    tasks = res.json()
    l_task = []
    for task in tasks:
        if task.get('completed') is True:
            l_task.append(task)

    print("({}/{}):".format(len(l_task), len(tasks)))
    for task in l_task:
        print("\t {}".format(task.get("title")))
