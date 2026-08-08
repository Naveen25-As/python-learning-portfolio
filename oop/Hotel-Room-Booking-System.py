# Hotel Room Booking System.

class Room:
    def __init__(self, room_number, room_type, price):
        self.room_number = room_number
        self.room_type = room_type
        self.price = price
        self.is_booked = False

    def book_room(self):
        if not self.is_booked:
            self.is_booked = True
            print(f"Room {self.room_number} has been booked.")
        else:
            print(f"Room {self.room_number} is already booked.")

    def cancel_booking(self):
        if self.is_booked:
            self.is_booked = False
            print(f"Booking for Room {self.room_number} has been canceled.")
        else:
            print(f"Room {self.room_number} is not booked.")

    def display_room_info(self):
        status = "Booked" if self.is_booked else "Available"
        print(f"Room Number: {self.room_number}, Type: {self.room_type}, Price: {self.price}, Status: {status}")
        
room1 = Room(101, "Single", 100)
room1.display_room_info()
room1.book_room()
room1.display_room_info()