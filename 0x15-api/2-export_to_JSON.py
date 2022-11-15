#!/usr/bin/python3
"""Gather data from an API
for a given employee ID, returns
information about his/her TO list progress.
export to csv
"""
import json
import requests
import sys

if __name__ == "__main__":
    inp = int(sys.argv[1])
    url = 'https://jsonplaceholder.typicode.com/users'
    url2 = 'https://jsonplaceholder.typicode.com/todos'
    payload1 = {'id': inp}
    payload2 = {'userId': inp}
    r_user = requests.get(url, params=payload1)
    r_todos = requests.get(url2, params=payload2)
    r_user_dict = r_user.json()
    r_todos_dict = r_todos.json()
    uname = r_user_dict[0]["username"]

    with open("{}.json".format(inp), "w") as jsonfile:
        json.dump({inp: [{
                "task": item.get("title"),
                "completed": item.get("completed"),
                "username": uname
            } for item in r_todos_dict]}, jsonfile)
