#!/usr/bin/python3
"""Gather data from an API
"""
import requests
import sys


if __name__ == "__main__":
    inp = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/users'
    url2 = 'https://jsonplaceholder.typicode.com/todos'
    payload1 = {'id': inp}
    payload2 = {'userId': inp}
    r_user = requests.get(url, params=payload1)
    r_todos = requests.get(url2, params=payload2)
    r_user_dict = r_user.json()
    r_todos_dict = r_todos.json()
    ename = r_user_dict[0]["name"]
    tnot = len(r_todos_dict)
    res = 0
    for item in r_todos_dict:
        if item.get('completed') is True:
            res = res + 1

    nofdt = res
    print("{} is done with tasks({}/{}):".format(ename, nofdt, tnot))
    for item in r_todos_dict:
        if item.get('completed') is True:
            print("\t {}".format(item.get('title')))
