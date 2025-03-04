#! /usr/bin/python3

import requests
import os
import passwords

MY_USER = passwords.user
MY_PASS = passwords.passwd

response = requests.get("http://192.168.0.247:8080/basic-auth/russ/test", auth=(MY_USER,MY_PASS))

print(response.text)

