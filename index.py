import sys
from controllers.controller import Controller

command = sys.argv[1]
command_input = sys.argv[2:]
# print(command, command_input)

if command == "create_parking_lot":
  Controller.create_parking_lot(command_input[0])
elif command == "park":
  Controller.park(command_input[0])
elif command == "leave":
  Controller.leave(command_input[0], command_input[1])
