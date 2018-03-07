#!/usr/bin/env python3
import json
from library._utils import json_to_dict
from library.password import compare_hash
import getpass


def auth_user(username, password):
    users = json_to_dict("users.json")
    if username in users:
        user = users[username]
        return compare_hash(user.get("password"), password)
    return False


if __name__ == "__main__":
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    is_auth = auth_user(username, password)
    print(is_auth)
