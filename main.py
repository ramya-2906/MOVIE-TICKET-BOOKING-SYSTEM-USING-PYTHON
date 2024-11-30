from MovieTicketBooking import MovieTicketBooking
def main():
    system = MovieTicketBooking()

    while True:
        print("\n-------------------------")
        print("Hi, Welcome to the Theatre")
        print("-------------------------")
        print("1. Book a Ticket")
        print("2. View All Shows")
        print("3. Cancel Tickets")
        print("4. Update the Movie")
        print("5. Exit")
        
        choice = input("\nEnter your choice: ")

        if choice == '1':
            system.book_ticket()
        elif choice == '2':
            system.view_all_shows()
        elif choice == '3':
            system.cancel_ticket()
        elif choice == '4':
            system.update_movie()
        elif choice == '5':
            print("Thank you for using the Movie Ticket Booking System!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()

