from abc import ABC, abstractmethod

# Abstract base class for the Ticket Booking System
class TicketBookingSystem(ABC):
    
    @abstractmethod
    def display_movies(self):
        pass
    
    @abstractmethod
    def book_ticket(self):
        pass
    
    @abstractmethod
    def view_all_shows(self):
        pass
    
    @abstractmethod
    def cancel_ticket(self):
        pass
    
    @abstractmethod
    def update_movie(self):
        pass
