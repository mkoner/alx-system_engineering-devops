#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    my_url = "https://jsonplaceholder.typicode.com/"
    my_users = requests.get(my_url + "users/{}".format(sys.argv[1])).json()
    my_todos = requests.get(my_url + "todos", params={"userId": sys.argv[1]}).json()

    comp = [t.get("title") for t in my_todos if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        my_users.get("name"), len(comp), len(my_todos)))
    [print("\t {}".format(c)) for c in comp]