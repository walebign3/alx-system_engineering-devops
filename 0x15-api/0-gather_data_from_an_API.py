#!/usr/bin/python3
"""
Python script that, using this REST API
for a given employee ID, returns information
"""
import requests
import sys


if __name__ == "__main__":
    i = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/users'
    url2 = 'https://jsonplaceholder.typicode.com/todos'
    payload1 = {'id': i}
    payload2 = {'userId': i}
    r_user = requests.get(url, params=payload1)
    r_todos = requests.get(url2, params=payload2)
    r_user_dict = r_user.json()
    r_todos_dict = r_todos.json()
    E_NAME = r_user_dict[0]["name"]
    T_N_OF_T = len(r_todos_dict)
    res = 0
    for item in r_todos_dict:
        if item.get('completed') is True:
            res = res + 1
    N_OF_D_T = res
    print('{} is done with tasks({}/{}):'.format(E_NAME, N_OF_D_T, T_N_OF_T))
    for item in r_todos_dict:
        if item.get('completed') is True:
            print('\t {}'.format(item.get('title')))
