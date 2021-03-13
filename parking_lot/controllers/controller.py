from models.model import ParkingLot
from views.view import View

class Controller:
  @staticmethod
  def create_parking_lot(capacity): 
    ParkingLot.create(capacity)
    View.create_parking_lot(capacity)

  
  @staticmethod
  def park(plate_number):
    allocated_slot_number = ParkingLot.park(plate_number)
    if allocated_slot_number == 0:
      View.full()
    else:
      View.park(allocated_slot_number)

  @staticmethod
  def leave(plate_number, hours):
    result = ParkingLot.leave(plate_number, hours)
    
    if result == False:
      View.not_found(plate_number)
    else:
      charge = result["charge"]
      slot_number = result["ParkingLot"].slot_number
      # print(plate_number)
      View.leave(slot_number, plate_number, charge )
    

  @staticmethod
  def status():
    data = ParkingLot.read()
    message = ""
    for i in data:
      if(i.plate_number == ""):
        continue
      message = message + f"{i.slot_number}   {i.plate_number} \r\n"
    View.status(message)
  