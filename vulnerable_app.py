import subprocess
import pickle

username = input("Enter username: ")
password = input("Enter password: ")

ADMIN_PASSWORD = "admin123" 

if password == ADMIN_PASSWORD:
    print("Login Successful")
else:
    print("Login Failed")

command = input("Enter a system command: ")
subprocess.call(command, shell=True)

data = input("Enter serialized data file: ")

with open(data, "rb") as file:
    obj = pickle.load(file)

code = input("Enter Python expression: ")
result = eval(code)

print(result)
