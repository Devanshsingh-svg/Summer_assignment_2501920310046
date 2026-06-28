class TicketBooking:
    def __init__(self, total_seats: int):
        self.available = total_seats
    def book(self, count: int) -> bool:
        if count <= self.available:
            self.available -= count
            return True
        return False

if __name__ == "__main__":
    tb = TicketBooking(50)
    print("Booking 5 tickets:", tb.book(5))
