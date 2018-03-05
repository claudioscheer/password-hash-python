#!/usr/bin/env python3
from library.password import get_hash, get_salt, compare_hash
from library._utils import json_to_dict, save_file_json


username = input("Username: ")
password = input("Password: ")

hash = get_hash(password, get_salt())
users = json_to_dict("users.json")
users[username] = {
    "password": hash
}
save_file_json("users.json", users)
print("User saved.")