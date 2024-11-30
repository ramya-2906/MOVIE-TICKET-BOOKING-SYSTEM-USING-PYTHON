from TicketBookingSystem import TicketBookingSystem
class MovieTicketBooking(TicketBookingSystem):
    
    class Movie:
        def __init__(self, title, show_times):
            self.title = title
            self.show_times = show_times
            self.price_per_ticket = 200

    def __init__(self):
        # List of movies available in the system
        self.movies = [
            self.Movie("Pushpa 2", ["12:00 PM", "3:00 PM", "6:00 PM", "9:00 PM"]),
            self.Movie("Game Changer", ["11:00 AM", "2:00 PM", "5:00 PM", "8:00 PM"]),
            self.Movie("Raja Saab", ["1:00 PM", "4:00 PM", "7:00 PM"]),
            self.Movie("Ustaad Bagat Singh", ["12:00 PM", "3:00 PM", "6:00 PM", "9:00 PM"]),
            self.Movie("Kannappa", ["11:00 AM", "2:00 PM", "5:00 PM", "8:00 PM"]),
            self.Movie("Vishwambara", ["1:00 PM", "4:00 PM", "7:00 PM"])
        ]
        self.bookings = []

    def display_movies(self):
        print("\nAvailable Movies:")
        for index, movie in enumerate(self.movies, start=1):
            print(f"{index}. {movie.title}")

    def book_ticket(self):
        self.display_movies()
        try:
            movie_choice = int(input("\nEnter the number of the movie you want to watch: "))
            movie = self.movies[movie_choice - 1]
            print(f"Selected Movie: {movie.title}")
            print(f"Show Times: {', '.join(movie.show_times)}")
            
            show_time = input("\nEnter the show time you want: ")
            if show_time not in movie.show_times:
                print("Invalid show time.")
                return
            
            tickets = int(input("\nEnter the number of tickets you want to buy: "))
            total_price = movie.price_per_ticket * tickets
            print(f"\nBooking Confirmed! Total Price: {total_price}")
            self.bookings.append({"Movie": movie.title, "Show Time": show_time, "Tickets": tickets})
        except (ValueError, IndexError):
            print("Invalid input, please try again.")

    def view_all_shows(self):
        if not self.movies:
            print("\nNo shows available.")
            return
        
        print("\nAll Available Movies and Showtimes:")
        for movie in self.movies:
            print(f"\n{movie.title}:")
            for show_time in movie.show_times:
                print(f" - {show_time}")

    def cancel_ticket(self):
        if not self.bookings:
            print("\nNo bookings to cancel.")
            return

        print("\nExisting Bookings:")
        for idx, booking in enumerate(self.bookings, start=1):
            print(f"{idx}. {booking['Movie']} at {booking['Show Time']} ({booking['Tickets']} tickets)")

        try:
            booking_id = int(input("\nEnter the booking number you want to cancel: "))
            cancelled_booking = self.bookings.pop(booking_id - 1)
            print(f"\nBooking for {cancelled_booking['Movie']} at {cancelled_booking['Show Time']} has been cancelled.")
        except (ValueError, IndexError):
            print("Invalid booking number!")

    def update_movie(self):
        self.display_movies()
        try:
            movie_choice = int(input("\nEnter the movie number to update: "))
            movie = self.movies[movie_choice - 1]
            print(f"Selected Movie: {movie.title}")
            new_show_time = input("\nEnter a new showtime to add (leave blank to skip): ")
            if new_show_time:
                movie.show_times.append(new_show_time)
                print(f"\nNew showtime added for {movie.title}: {new_show_time}")
            else:
                print("No update made.")
        except (ValueError, IndexError):
            print("Invalid movie number!")


