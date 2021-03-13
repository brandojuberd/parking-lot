class View:
  @staticmethod
  def create_parking_lot(capacity):
    print(f"Created parking lot with {capacity} slots")
  
  @staticmethod
  def park(allocated_lot_number):
    print(f"Allocated slot number: {allocated_lot_number}")

  @staticmethod
  def full():
    print(f"Sorry, parking lot is full")
  
  @staticmethod
  def leave(slot_number, plate_number, charge):
    print(f"Registration number {plate_number} with Slot Number {slot_number} is free with Charge {charge}")
  
  @staticmethod
  def not_found(plate_number):
    print(f"Registration number {plate_number} not found")