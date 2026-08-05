# Movie Ticket Booking System

class MovieTicket:
    def __init__(self, movie_name, ticket_price):
        self.movie_name = movie_name
        self.ticket_price = ticket_price

    def book_ticket(self, quantity):
        total = quantity * self.ticket_price
        print("Movie:", self.movie_name)
        print("Ticket Price:", self.ticket_price)
        print("Number of Tickets:", quantity)
        print("Total Amount:", total)


# Creating object
ticket = MovieTicket("Inception", 10.0)

# Booking tickets
ticket.book_ticket(3)