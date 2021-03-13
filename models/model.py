import json

class ParkingLot:
  def __init__(self, slot_number, plate_number=""):
    self.__slot_number = slot_number
    self.__plate_number = plate_number

  @property
  def slot_number(self):
    return self.__slot_number

  @slot_number.setter
  def slot_number(self, value):
    self.__slot_number = value

  @property
  def plate_number(self):
    return self.__plate_number

  @plate_number.setter
  def plate_number(self, value):
    self.__slot_number = value

  @staticmethod
  def create(capacity):
    list_of_lot = []
    for i in range(int(capacity)):
      list_of_lot.append(ParkingLot(i+1, ))
    ParkingLot.save(list_of_lot)
    

  @staticmethod
  def read():
    with open("./data/data.json", "r") as read_file:
      # print(data.read())
      data = json.load(read_file)
      list_of_class = []
      for lot in data:
        list_of_class.append(ParkingLot(lot["slot_number"], lot["plate_number"]))
      return list_of_class

  @staticmethod
  def save(data):
    data_json = []
    for i in data:
      data_json.append(
        {
          "slot_number": i.slot_number,
          "plate_number": i.plate_number
        }
      )
    with open("./data/data.json", "w") as write_file:
      json.dump(data_json, write_file, indent= 2)
  