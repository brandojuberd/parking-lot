import sys
from controllers.controller import Controller

command = sys.argv[1]
command_input = sys.argv[2:]
print(command, command_input)

if command == "create_parking_lot":
    Controller.create_parking_lot(command_input[0])
    print("wait")