import subprocess
import ast
import json
import os

username = input("Enter username: ")
password = input("Enter password: ")

ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")

if password == ADMIN_PASSWORD:
    print("Login Successful")
else:
    print("Login Failed")


command = input("Enter a command: ")

allowed_commands = ["whoami", "date", "hostname"]

if command in allowed_commands:
    result = subprocess.run(
        [command],
        capture_output=True,
        text=True
    )
    print(result.stdout)

else:
    print("Command not allowed")

filename = input("Enter JSON file name: ")

try:
    with open(filename, "r") as file:
        data = json.load(file)

    print(data)

except FileNotFoundError:
    print("File not found")
except json.JSONDecodeError:
    print("Invalid JSON file")

expression = input("Enter a value: ")

try:
    result = ast.literal_eval(expression)
    print(result)

except (ValueError, SyntaxError):
    print("Invalid input")
