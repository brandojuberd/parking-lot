from models.model import ParkingLot

class Controller:
  @staticmethod
  def create_parking_lot(capacity): 
    ParkingLot.create(capacity)
    print("In Controller")