import sys
from controllers.controller import Controller

command = sys.argv[1]
print(command)

if command == "park":
    Controller.park()
    print("wait")