import os
import tkinter
import tkinter.messagebox as tkmb
import customtkinter as ctk
import csv
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from CTkListbox import *

# classes
class Event:
    events_list = []  # Class variable to store events

    def __init__(self, event_id, name, date, venue, Ticket):
        self.event_id = event_id
        self.name = name
        self.date = date
        self.venue = venue
        self.Ticket = Ticket
        Event.events_list.append(self)  # Append the event to events_list

    def __str__(self):
        return f"{self.name} on {self.date} at {self.venue}"

    @classmethod
    def get_all_events(cls):
        # Define the paths for all CSV files
        Event.events_list = []
        csv_files = ["csv/CinemaEvent.csv", "csv/SportsEvent.csv", "csv/ConcertEvent.csv"]

        # Iterate over each CSV file
        for csv_file in csv_files:
            # Check if the CSV file exists
            if os.path.exists(csv_file):
                with open(csv_file, mode='r') as file:
                    reader = csv.reader(file)
                    next(reader)  # Skip the header row
                    for row in reader:
                        # Extract data from the row
                        event_type = row[0]
                        event_id = int(row[1])
                        name = row[2]
                        date = row[3]
                        venue = row[4]
                        ticket_info = Ticket(Event, int(row[-4]), int(row[-3]), int(row[-2]), int(row[-1]))

                        # Create instances based on event type
                        if event_type == "CinemaEvent":
                            event = CinemaEvent(event_id, name, date, venue, row[5], row[6], row[7], ticket_info, False)
                        elif event_type == "SportsEvent":
                            event = SportsEvent(event_id, name, date, venue, row[5], row[6], row[7], ticket_info, False)
                        elif event_type == "ConcertEvent":
                            event = ConcertEvent(event_id, name, date, venue, row[5], row[6], row[7], ticket_info, False)
                        else:
                            # Handle unknown event types
                            print(f"Unknown event type: {event_type}")
                            continue
                        
        return Event.events_list
   
class CinemaEvent(Event):
    def __init__(self, event_id, name, date, venue, movie_title, genre, duration, Ticket, write=True):
        super().__init__(event_id, name, date, venue, Ticket)
        self.movie_title = movie_title
        self.genre = genre
        self.duration = duration

        if write:
            with open("csv/CinemaEvent.csv", mode='a', newline='') as file:
                writer = csv.writer(file)
                #writer.writerow(["Event_Type", "Event_ID", "Name", "Date", "Venue", "Movie_Title", "Genre", "Duration", "VIP_tickets_available", "VIP_ticket_price", "Regular_tickets_available", "Regular_ticket_price"])
                writer.writerow(["CinemaEvent", event_id, name, date, venue, movie_title, genre, duration, Ticket.VIP_tickets_available, Ticket.VIP_price, Ticket.Regular_tickets_available, Ticket.Regular_price])
 
    def delete_event(self, event_id):
        # Read all rows from the CSV file and store them in a list
        with open("csv/CinemaEvent.csv", mode='r', newline='') as file:
            reader = csv.reader(file)
            rows = list(reader)

         # Find the row corresponding to the event to be deleted
        for row in rows:
            if row[0] == "CinemaEvent" and int(row[1]) == int(event_id):
                rows.remove(row)
                break

         # Write the updated rows back to the CSV file
        with open("csv/CinemaEvent.csv", mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
            
        Event.events_list.remove(self)
    
    def update_event(self, name, date, venue, ticket, movie_title, genre, duration):
        # Update instance attributes
        self.name = name
        self.date = date
        self.venue = venue
        self.Ticket = ticket
        self.movie_title = movie_title
        self.genre = genre
        self.duration = duration

        # Read all rows from the CSV file and store them in a list
        with open("csv/CinemaEvent.csv", mode='r', newline='') as file:
            reader = csv.reader(file)
            rows = list(reader)

        # Find the row corresponding to the event to be updated
        for row in rows:
            if row[0] == "CinemaEvent" and int(row[1]) == int(self.event_id):
                # Update the row with the new data
                row[2] = name
                row[3] = date
                row[4] = venue
                row[5] = movie_title
                row[6] = genre
                row[7] = duration
                row[8] = ticket.VIP_tickets_available
                row[9] = ticket.VIP_price
                row[10] = ticket.Regular_tickets_available
                row[11] = ticket.Regular_price
                break

        # Write the updated rows back to the CSV file
        with open("csv/CinemaEvent.csv", mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
            
    def __str__(self):
        # return super().__str__() + f" - Movie: {self.movie_title} - Genre: {self.genre} - Duration: {self.duration} - Rating: {self.rating} - VIP tickets: {self.Ticket.VIP_tickets_available} for ${self.Ticket.VIP_price} - Regular tickets: {self.Ticket.Regular_tickets_available} for ${self.Ticket.Regular_price}"
        return super().__str__() + f" - Movie: {self.movie_title} - Genre: {self.genre} - Duration: {self.duration}"

class SportsEvent(Event):
    def __init__(self, event_id, name, date, venue, sport_type, game_type, duration, Ticket, write=True):
        super().__init__(event_id, name, date, venue, Ticket)
        self.sport_type = sport_type
        self.game_type = game_type
        self.duration = duration
        
        if write:
            with open("csv/SportsEvent.csv", mode='a', newline='') as file:
                writer = csv.writer(file)
                #writer.writerow(["Event_Type", "Event_ID", "Name", "Date", "Venue", "Sport_Type", "Game_Type", "Duration", "VIP_tickets_available", "VIP_ticket_price", "Regular_tickets_available", "Regular_ticket_price"])
                writer.writerow(["SportsEvent", event_id, name, date, venue, sport_type, game_type, duration, Ticket.VIP_tickets_available, Ticket.VIP_price, Ticket.Regular_tickets_available, Ticket.Regular_price])
        
    def update_event(self, name, date, venue, ticket, sport_type, game_type, duration):
        # Update instance attributes
        self.name = name
        self.date = date
        self.venue = venue
        self.Ticket = ticket
        self.sport_type = sport_type
        self.game_type = game_type
        self.duration = duration

        # Read all rows from the CSV file and store them in a list
        with open("csv/SportsEvent.csv", mode='r', newline='') as file:
            reader = csv.reader(file)
            rows = list(reader)

        # Find the row corresponding to the event to be updated
        for row in rows:
            if row[0] == "SportsEvent" and int(row[1]) == int(self.event_id):
                # Update the row with the new data
                row[2] = name
                row[3] = date
                row[4] = venue
                row[5] = sport_type
                row[6] = game_type
                row[7] = duration
                row[8] = ticket.VIP_tickets_available
                row[9] = ticket.VIP_price
                row[10] = ticket.Regular_tickets_available
                row[11] = ticket.Regular_price
                break

        # Write the updated rows back to the CSV file
        with open("csv/SportsEvent.csv", mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
            
    def __str__(self):
        # return super().__str__() + f" - Sport: {self.sport_type} - Duration: {self.duration} - VIP tickets: {self.Ticket.VIP_tickets_available} for ${self.Ticket.VIP_price} - Regular tickets: {self.Ticket.Regular_tickets_available} for ${self.Ticket.Regular_price}"
        return super().__str__() + f" - Sport: {self.sport_type} - Competetion: {self.game_type} - Duration: {self.duration}"

class ConcertEvent(Event):
    def __init__(self, event_id, name, date, venue, artist_band, genre, duration, Ticket, write=True):
        super().__init__(event_id, name, date, venue, Ticket)
        self.artist_band = artist_band
        self.genre = genre
        self.duration = duration

        if write:
            with open("csv/ConcertEvent.csv", mode='a', newline='') as file:
                writer = csv.writer(file)
                #writer.writerow(["Event_Type", "Event_ID", "Name", "Date", "Venue", "Artist/Band", "Genre", "Duration", "VIP_tickets_available", "VIP_ticket_price", "Regular_tickets_available", "Regular_ticket_price"])
                writer.writerow(["ConcertEvent",event_id, name, date, venue, artist_band, genre, duration, Ticket.VIP_tickets_available, Ticket.VIP_price, Ticket.Regular_tickets_available, Ticket.Regular_price])

    def update_event(self, name, date, venue, ticket, artist_band, genre, duration):
        # Update instance attributes
        self.name = name
        self.date = date
        self.venue = venue
        self.Ticket = ticket
        self.artist_band = artist_band
        self.genre = genre
        self.duration = duration

        # Read all rows from the CSV file and store them in a list
        with open("csv/ConcertEvent.csv", mode='r', newline='') as file:
            reader = csv.reader(file)
            rows = list(reader)

        # Find the row corresponding to the event to be updated
        for row in rows:
            if row[0] == "ConcertEvent" and int(row[1]) == int(self.event_id):
                # Update the row with the new data
                row[2] = name
                row[3] = date
                row[4] = venue
                row[5] = artist_band
                row[6] = genre
                row[7] = duration
                row[8] = ticket.VIP_tickets_available
                row[9] = ticket.VIP_price
                row[10] = ticket.Regular_tickets_available
                row[11] = ticket.Regular_price
                break

        # Write the updated rows back to the CSV file
        with open("csv/ConcertEvent.csv", mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)

    def __str__(self):
        # return super().__str__() + f" - Band: {self.artist_band} - Genre: {self.genre} - Duration: {self.duration} - VIP tickets: {self.Ticket.VIP_tickets_available} for ${self.Ticket.VIP_price} - Regular tickets: {self.Ticket.Regular_tickets_available} for ${self.Ticket.Regular_price}"
        return super().__str__() + f" - Performer: {self.artist_band} - Genre: {self.genre} - Duration: {self.duration}"

class Ticket:
    def __init__(self, Event, VIP_tickets_available, VIP_price, Regular_tickets_available, Regular_price):
        self.Event = Event
        self.VIP_price = VIP_price
        self.Regular_price = Regular_price
        self.VIP_tickets_available = VIP_tickets_available
        self.Regular_tickets_available = Regular_tickets_available

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Admin Panel")
        w, h = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry("%dx%d+0+0" % (w, h))

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=1)
        self.grid_rowconfigure((0, 1, 2, 3), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = ctk.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="Admin Panel", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = ctk.CTkButton(self.sidebar_frame, text="Manage Events", command=lambda: self.show_frame("events"))
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = ctk.CTkButton(self.sidebar_frame, text="Manage Users", command=lambda: self.show_frame("users"))
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = ctk.CTkButton(self.sidebar_frame, text="View Analytics", command=lambda: self.show_frame("analytics"))
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.sidebar_button_4 = ctk.CTkButton(self.sidebar_frame, text="Logout", fg_color="red", command=self.logout)
        self.sidebar_button_4.grid(row=7, column=0, padx=20, pady=10)

        # Create frames for each section
        self.frames = {}
        self.frames["events"] = self.create_events_frame()
        self.frames["users"] = self.create_users_frame()
        self.frames["analytics"] = self.create_analytics_frame()

        # Show the default frame
        self.show_frame("events")

        # Create tabview and radiobutton frame
        # self.create_misc_widgets()

    def show_frame(self, frame_name):
        frame = self.frames[frame_name]
        frame.tkraise()

    def create_events_frame(self):
        # Frame for managing events
        events_frame = ctk.CTkFrame(self)
        events_frame.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew", rowspan=4)

        ticket_display_frame = ctk.CTkFrame(events_frame)
        ticket_display_frame.grid(row=0, column=0, padx=(20, 0), pady=(20, 0), sticky="nsew")

        ticket_display_label = ctk.CTkLabel(ticket_display_frame, text="Current Events:", font=ctk.CTkFont(size=20, weight="bold"), width=400)
        ticket_display_label.grid(row=0, column=0, padx=20, pady=(10,0))

        self.event_listbox = CTkListbox(ticket_display_frame, height=300, width=840)
        self.event_listbox.grid(row=1, column=0, padx=20, pady=10)
        self.populate_event_listbox()
        self.event_listbox.bind("<<ListboxSelect>>", self.on_event_selected)

        event_creation_frame = ctk.CTkFrame(events_frame)
        event_creation_frame.grid(row=1, column=0, padx=(20, 0), pady=(20, 0), sticky="nsew")

        self.create_event_widgets(event_creation_frame)

        return events_frame

    def create_event_widgets(self, frame):
        # Widgets for event creation and modification
        self.event_id_label = ctk.CTkLabel(frame, text="Event ID:", font=ctk.CTkFont(size=17, weight="bold"))
        self.event_id_label.grid(row=0, column=0, padx=20, pady=10)
        self.event_id_entry = ctk.CTkEntry(frame, font=ctk.CTkFont(size=17, weight="bold"), width=250)
        self.event_id_entry.grid(row=0, column=1, padx=20, pady=10)

        self.event_name_label = ctk.CTkLabel(frame, text="Event Name:", font=ctk.CTkFont(size=17, weight="bold"))
        self.event_name_label.grid(row=1, column=0, padx=20, pady=10)
        self.event_name_entry = ctk.CTkEntry(frame, font=ctk.CTkFont(size=17, weight="bold"), width=250)
        self.event_name_entry.grid(row=1, column=1, padx=20, pady=10)

        self.event_date_label = ctk.CTkLabel(frame, text="Event Date:", font=ctk.CTkFont(size=17, weight="bold"))
        self.event_date_label.grid(row=2, column=0, padx=20, pady=10)
        self.event_date_entry = ctk.CTkEntry(frame, font=ctk.CTkFont(size=17, weight="bold"), width=250)
        self.event_date_entry.grid(row=2, column=1, padx=20, pady=10)

        self.event_venue_label = ctk.CTkLabel(frame, text="Event Venue:", font=ctk.CTkFont(size=17, weight="bold"))
        self.event_venue_label.grid(row=3, column=0, padx=20, pady=10)
        self.event_venue_entry = ctk.CTkEntry(frame, font=ctk.CTkFont(size=17, weight="bold"), width=250)
        self.event_venue_entry.grid(row=3, column=1, padx=20,pady=10)

        self.event_type_label = ctk.CTkLabel(frame, text="Event Type:", font=ctk.CTkFont(size=17, weight="bold"))
        self.event_type_label.grid(row=4, column=0, padx=20, pady=10)
        self.event_type_entry = ctk.CTkComboBox(frame, values=["Cinema", "Sports", "Concert"], command=self.type_change, font=ctk.CTkFont(size=17), width=250)
        self.event_type_entry.grid(row=4, column=1, padx=20,pady=10)

        self.first_extra_label = ctk.CTkLabel(frame, text="Movie Title:", font=ctk.CTkFont(size=17, weight="bold"))
        self.first_extra_label.grid(row=5, column=0, padx=20, pady=10)
        self.first_extra_entry = ctk.CTkEntry(frame, font=ctk.CTkFont(size=17, weight="bold"), width=250)
        self.first_extra_entry.grid(row=5, column=1, padx=20,pady=10)

        self.tickets_amount_label = ctk.CTkLabel(frame, text="Tickets Amount:", font=ctk.CTkFont(size=17, weight="bold"))
        self.tickets_amount_label.grid(row=0, column=2, padx=20, pady=10)
        self.tickets_amount_entry = ctk.CTkEntry(frame, font=ctk.CTkFont(size=17, weight="bold"), width=250)
        self.tickets_amount_entry.grid(row=0, column=3, padx=20, pady=10)

        self.tickets_price_label = ctk.CTkLabel(frame, text="Tickets Price:", font=ctk.CTkFont(size=17, weight="bold"))
        self.tickets_price_label.grid(row=1, column=2, padx=20, pady=10)
        self.tickets_price_entry = ctk.CTkEntry(frame, font=ctk.CTkFont(size=17, weight="bold"), width=250)
        self.tickets_price_entry.grid(row=1, column=3, padx=20, pady=10)

        self.vip_amount_label = ctk.CTkLabel(frame, text="VIP Amount:", font=ctk.CTkFont(size=17, weight="bold"))
        self.vip_amount_label.grid(row=2, column=2, padx=20, pady=10)
        self.vip_amount_entry = ctk.CTkEntry(frame, font=ctk.CTkFont(size=17, weight="bold"), width=250)
        self.vip_amount_entry.grid(row=2, column=3, padx=20, pady=10)

        self.vip_price_label = ctk.CTkLabel(frame, text="VIP Price:", font=ctk.CTkFont(size=17, weight="bold"))
        self.vip_price_label.grid(row=3, column=2, padx=20, pady=10)
        self.vip_price_entry = ctk.CTkEntry(frame, font=ctk.CTkFont(size=17, weight="bold"), width=250)
        self.vip_price_entry.grid(row=3, column=3, padx=20, pady=10)
        
        self.second_extra_label = ctk.CTkLabel(frame, text="Genre:", font=ctk.CTkFont(size=17, weight="bold"))
        self.second_extra_label.grid(row=4, column=2, padx=20, pady=10)
        self.second_extra_entry = ctk.CTkEntry(frame, font=ctk.CTkFont(size=17, weight="bold"), width=250)
        self.second_extra_entry.grid(row=4, column=3, padx=20,pady=10)
        
        self.third_extra_label = ctk.CTkLabel(frame, text="Duration:", font=ctk.CTkFont(size=17, weight="bold"))
        self.third_extra_label.grid(row=5, column=2, padx=20, pady=10)
        self.third_extra_entry = ctk.CTkEntry(frame, font=ctk.CTkFont(size=17, weight="bold"), width=250)
        self.third_extra_entry.grid(row=5, column=3, padx=20,pady=10)

        self.create_event_button = ctk.CTkButton(frame, text="Create Event", fg_color="green", hover_color="black", font=ctk.CTkFont(size=17, weight="bold"), width=400, command=self.submit_event)
        self.create_event_button.grid(row=6, column=0, columnspan=2, padx=20, pady=(10, 0))
        
        self.update_event_button = ctk.CTkButton(frame, text="Update Event", font=ctk.CTkFont(size=17, weight="bold"), width=400, command=self.update_event, state="disabled")
        self.update_event_button.grid(row=6, column=2, columnspan=2, padx=20, pady=(10, 0))
        
        self.delete_event_button = ctk.CTkButton(frame, text="Delete Event", fg_color="darkred", hover_color="black", font=ctk.CTkFont(size=17, weight="bold"), width=400, command=self.delete_event, state="disabled")
        self.delete_event_button.grid(row=7, column=2, columnspan=2, padx=20, pady=10)
        
        # initialize ticket display
        self.update_events_list()

    def create_users_frame(self):
        # Frame for managing users
        users_frame = ctk.CTkFrame(self)
        users_frame.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew", rowspan=4)

        user_display_frame = ctk.CTkFrame(users_frame)
        user_display_frame.grid(row=0, column=0, padx=(20, 0), pady=(20, 0), sticky="nsew")

        user_display_label = ctk.CTkLabel(user_display_frame, text="Current Users:", font=ctk.CTkFont(size=20, weight="bold"), width=400)
        user_display_label.grid(row=0, column=0, padx=20, pady=(10, 0))

        self.user_listbox = CTkListbox(user_display_frame, height=250, width=840)
        self.user_listbox.grid(row=1, column=0, padx=20, pady=10)
        self.populate_user_listbox()
        self.user_listbox.bind("<<ListboxSelect>>", self.on_user_selected)

        user_management_frame = ctk.CTkFrame(users_frame)
        user_management_frame.grid(row=1, column=0, padx=(20, 0), pady=(20, 0), sticky="nsew")

        self.create_user_widgets(user_management_frame)

        return users_frame

    def create_user_widgets(self, frame):
        # Widgets for user management        
        self.username_label = ctk.CTkLabel(frame, text="Username:", font=ctk.CTkFont(size=17, weight="bold"))
        self.username_label.grid(row=0, column=0, padx=20, pady=10)
        self.username_entry = ctk.CTkEntry(frame, font=ctk.CTkFont(size=17, weight="bold"), width=250)
        self.username_entry.grid(row=0, column=1, padx=20, pady=10)

        self.password_label = ctk.CTkLabel(frame, text="Password:", font=ctk.CTkFont(size=17, weight="bold"))
        self.password_label.grid(row=1, column=0, padx=20, pady=10)
        self.password_entry = ctk.CTkEntry(frame, font=ctk.CTkFont(size=17, weight="bold"), width=250)
        self.password_entry.grid(row=1, column=1, padx=20, pady=10)
        
        self.age_label = ctk.CTkLabel(frame, text="Age:", font=ctk.CTkFont(size=17, weight="bold"))
        self.age_label.grid(row=2, column=0, padx=20, pady=10)
        self.age_entry = ctk.CTkEntry(frame, font=ctk.CTkFont(size=17, weight="bold"), width=250)
        self.age_entry.grid(row=2, column=1, padx=20, pady=10)

        self.gender_label = ctk.CTkLabel(frame, text="Gender:", font=ctk.CTkFont(size=17, weight="bold"))
        self.gender_label.grid(row=3, column=0, padx=20, pady=10)
        self.gender_entry = ctk.CTkEntry(frame, font=ctk.CTkFont(size=17, weight="bold"), width=250)
        self.gender_entry.grid(row=3, column=1, padx=20, pady=10)

        self.role_label = ctk.CTkLabel(frame, text="Role:", font=ctk.CTkFont(size=17, weight="bold"))
        self.role_label.grid(row=4, column=0, padx=20, pady=10)
        self.role_entry = ctk.CTkComboBox(frame, values=["admin", "user"], font=ctk.CTkFont(size=17), width=250)
        self.role_entry.grid(row=4, column=1, padx=20, pady=10)

        self.add_user_button = ctk.CTkButton(frame, text="Create User", fg_color="green", hover_color="black", font=ctk.CTkFont(size=17, weight="bold"), width=400, command=self.add_user)
        self.add_user_button.grid(row=5, column=0, padx=20, pady=(10, 0))

        self.edit_user_button = ctk.CTkButton(frame, text="Edit User", font=ctk.CTkFont(size=17, weight="bold"), width=400, command=self.edit_user, state="disabled")
        self.edit_user_button.grid(row=5, column=1, padx=20, pady=(10, 0))

        self.delete_user_button = ctk.CTkButton(frame, text="Delete User", fg_color="darkred", hover_color="black", font=ctk.CTkFont(size=17, weight="bold"), width=400, command=self.delete_user, state="disabled")
        self.delete_user_button.grid(row=6, column=1, padx=20, pady=10)

    def create_analytics_frame(self):
        # Frame for analytics
        analytics_frame = ctk.CTkFrame(self, width=800, height=600)  # Adjust width and height as needed
        analytics_frame.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew", rowspan=4)

        analytics_display_frame = ctk.CTkFrame(analytics_frame)
        analytics_display_frame.grid(row=0, column=0, padx=20, pady=(20, 0), sticky="nsew")

        analytics_display_label = ctk.CTkLabel(analytics_display_frame, text="Current analytics:", font=ctk.CTkFont(size=20, weight="bold"), width=400)
        analytics_display_label.pack()

        analytics_management_frame = ctk.CTkFrame(analytics_frame, width=800, height=600)  # Adjust width and height as needed
        analytics_management_frame.grid(row=1, column=0, padx=(20, 0), pady=(20, 0), sticky="nsew")

        # Step 1: Read transactions.csv and extract Event IDs
        transactions_df = pd.read_csv("csv/transactions.csv")
        event_id_counts = transactions_df['Event ID'].value_counts()

        # Step 2: Read csv/CinemaEvent.csv, csv/ConcertEvent.csv, and csv/SportsEvent.csv
        cinema_df = pd.read_csv("csv/CinemaEvent.csv")
        concert_df = pd.read_csv("csv/ConcertEvent.csv")
        sports_df = pd.read_csv("csv/SportsEvent.csv")

        # Step 3: Count occurrences of Event IDs in each category
        cinema_event_counts = [event_id_counts.get(event_id, 0) for event_id in cinema_df['Event_ID']]
        concert_event_counts = [event_id_counts.get(event_id, 0) for event_id in concert_df['Event_ID']]
        sports_event_counts = [event_id_counts.get(event_id, 0) for event_id in sports_df['Event_ID']]

        # Create a separate frame for each graph
        cinema_frame = ctk.CTkFrame(analytics_management_frame, width=400, height=300)
        cinema_frame.grid(row=2, column=0, pady=10, padx=10, sticky="nsew")
        concert_frame = ctk.CTkFrame(analytics_management_frame, width=400, height=300)
        concert_frame.grid(row=2, column=1, pady=10, padx=10, sticky="nsew")
        sports_frame = ctk.CTkFrame(analytics_management_frame, width=400, height=300)
        sports_frame.grid(row=2, column=2, pady=10, padx=10, sticky="nsew")
        pie_chart_frame = ctk.CTkFrame(analytics_management_frame, width=800, height=600)
        pie_chart_frame.grid(row=3, column=0, columnspan=3, pady=10, padx=10, sticky="nsew")

        # Create a new figure with adjusted size for each subplot
        fig1, ax1 = plt.subplots(figsize=(5, 4))
        fig2, ax2 = plt.subplots(figsize=(5, 4))
        fig3, ax3 = plt.subplots(figsize=(5, 4))

        # CinemaEvent
        ax1.bar(cinema_df['Movie_Title'], cinema_event_counts, color='blue')
        ax1.set_title('Cinema Events')
        ax1.set_xlabel('Movie (Name)')
        ax1.set_ylabel('Tickets Bought (f)')

        # ConcertEvent
        ax2.bar(concert_df['Artist/Band'], concert_event_counts, color='green')
        ax2.set_title('Concert Events')
        ax2.set_xlabel('Band (Name)')
        ax2.set_ylabel('Tickets Bought (f)')

        # SportsEvent
        ax3.bar(sports_df['Game_Type'], sports_event_counts, color='red')
        ax3.set_title('Sports Events')
        ax3.set_xlabel('Match (Type)')
        ax3.set_ylabel('Tickets Bought (f)')
        
        # Step 4: Plot pie charts
        fig4, ax4 = plt.subplots(1, 3, figsize=(15, 5))

        # CinemaEvent
        ax4[0].pie(cinema_event_counts, labels=cinema_df['Movie_Title'], autopct='%1.1f%%', startangle=140)
        ax4[0].set_title('Cinema Events')

        # ConcertEvent
        ax4[1].pie(concert_event_counts, labels=concert_df['Artist/Band'], autopct='%1.1f%%', startangle=140)
        ax4[1].set_title('Concert Events')

        # SportsEvent
        ax4[2].pie(sports_event_counts, labels=sports_df['Game_Type'], autopct='%1.1f%%', startangle=140)
        ax4[2].set_title('Sports Events')

        plt.tight_layout()
        #plt.show()

        # Create a canvas to display each figure in the corresponding frame
        canvas1 = FigureCanvasTkAgg(fig1, master=cinema_frame)
        canvas1.draw()
        canvas1.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True)
        canvas2 = FigureCanvasTkAgg(fig2, master=concert_frame)
        canvas2.draw()
        canvas2.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True)
        canvas3 = FigureCanvasTkAgg(fig3, master=sports_frame)
        canvas3.draw()
        canvas3.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True)
        canvas4 = FigureCanvasTkAgg(fig4, master=pie_chart_frame)
        canvas4.draw()
        canvas4.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True)
                
        return analytics_frame
    
    def populate_event_listbox(self):
        self.event_listbox.delete(0, tkinter.END)
        for event in Event.events_list:
            self.event_listbox.insert(tkinter.END, event)

    def on_event_selected(self, event):
        selected_event = self.event_listbox.get(self.event_listbox.curselection())
        event_type = selected_event.__class__.__name__.replace("Event", "").replace("Event", "").replace("Event", "")
        
        self.update_event_button.configure(state="normal")
        self.delete_event_button.configure(state="normal")
        
        self.delete_inputs()
        
        self.event_id_entry.insert(0, selected_event.event_id)
        self.event_name_entry.insert(0, selected_event.name)
        self.event_date_entry.insert(0, selected_event.date)
        self.event_venue_entry.insert(0, selected_event.venue)
        self.event_type_entry.set(event_type)
        self.type_change(event_type)
        self.first_extra_entry.insert(0, getattr(selected_event, "movie_title", getattr(selected_event, "sport_type", getattr(selected_event, "artist_band", ""))))
        self.second_extra_entry.insert(0, getattr(selected_event, "genre", getattr(selected_event,"game_type", "")))
        self.third_extra_entry.insert(0, selected_event.duration)
        self.tickets_amount_entry.insert(0, selected_event.Ticket.Regular_tickets_available)
        self.tickets_price_entry.insert(0, selected_event.Ticket.Regular_price)
        self.vip_amount_entry.insert(0, selected_event.Ticket.VIP_tickets_available)
        self.vip_price_entry.insert(0, selected_event.Ticket.VIP_price)

    def update_events_list(self):
        self.event_listbox.delete(0, tkinter.END)
        events = Event.get_all_events()
        for event in events:
            self.event_listbox.insert(tkinter.END, event)

    def submit_event(self):
        event_id = self.event_id_entry.get()
        event_name = self.event_name_entry.get()
        event_date = self.event_date_entry.get()
        event_venue = self.event_venue_entry.get()
        tickets_amount = self.tickets_amount_entry.get()
        tickets_price = self.tickets_price_entry.get()
        vip_amount = self.vip_amount_entry.get()
        vip_price = self.vip_price_entry.get()
        type = self.event_type_entry.get()
        first_extra = self.first_extra_entry.get()
        second_extra = self.second_extra_entry.get()
        third_extra = self.third_extra_entry.get()

        if type == "Cinema":
            event = CinemaEvent(event_id, event_name, event_date, event_venue, first_extra, second_extra, third_extra, Ticket(Event, vip_amount, vip_price, tickets_amount, tickets_price))
        elif type == "Sports":
            event = SportsEvent(event_id, event_name, event_date, event_venue, first_extra, second_extra, third_extra, Ticket(Event, vip_amount, vip_price, tickets_amount, tickets_price))
        elif type == "Concert":
            event = ConcertEvent(event_id, event_name, event_date, event_venue, first_extra, second_extra, third_extra, Ticket(Event, vip_amount, vip_price, tickets_amount, tickets_price))

        tkmb.showinfo(title="Event Created Successfully", message=f"You have successfully created {event_name}")
        self.populate_event_listbox()

        self.delete_inputs()

    def update_event(self):
        selected_event = self.event_listbox.get(self.event_listbox.curselection())
        
        event_id = self.event_id_entry.get()
        event_name = self.event_name_entry.get()
        event_date = self.event_date_entry.get()
        event_venue = self.event_venue_entry.get()
        tickets_amount = self.tickets_amount_entry.get()
        tickets_price = self.tickets_price_entry.get()
        vip_amount = self.vip_amount_entry.get()
        vip_price = self.vip_price_entry.get()
        type = self.event_type_entry.get()
        first_extra = self.first_extra_entry.get()
        second_extra = self.second_extra_entry.get()
        third_extra = self.third_extra_entry.get()
        
        selected_event.update_event(event_name, event_date, event_venue, Ticket(Event, vip_amount, vip_price, tickets_amount, tickets_price), first_extra, second_extra, third_extra)

        tkmb.showinfo(title="Event Edited Successfully", message=f"You have successfully edited {event_name}")
        self.populate_event_listbox()

        self.delete_inputs()

    def delete_event(self):
        selected_event = self.event_listbox.get(self.event_listbox.curselection())

        event_id = self.event_id_entry.get()
        event_name = self.event_name_entry.get()

        selected_event.delete_event(event_id)
  
        tkmb.showinfo(title="Event Deleted Successfully", message=f"You have successfully deleted {event_name}")
        self.populate_event_listbox()

        self.delete_inputs()
        
    def delete_inputs(self):
        try:
            self.event_id_entry.delete(0, tkinter.END)
            self.event_name_entry.delete(0, tkinter.END)
            self.event_date_entry.delete(0, tkinter.END)
            self.event_venue_entry.delete(0, tkinter.END)
            self.first_extra_entry.delete(0, tkinter.END)
            self.second_extra_entry.delete(0, tkinter.END)
            self.third_extra_entry.delete(0, tkinter.END)
            self.tickets_amount_entry.delete(0, tkinter.END)
            self.tickets_price_entry.delete(0, tkinter.END)
            self.vip_amount_entry.delete(0, tkinter.END)
            self.vip_price_entry.delete(0, tkinter.END)
            self.username_entry.delete(0, "end")
            self.password_entry.delete(0, "end")
            self.age_entry.delete(0, "end")
            self.gender_entry.delete(0, "end")
            self.role_entry.set("")
        except:
            ""

    def populate_user_listbox(self):
        if os.path.exists("csv/users.csv"):
            with open("csv/users.csv", mode='r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0] != "Username":
                        self.user_listbox.insert("end", " - ".join(row))

    def on_user_selected(self, event):
        selected = self.user_listbox.get(self.user_listbox.curselection())
        details = selected.split(" - ")
        
        self.edit_user_button.configure(state="normal")
        self.delete_user_button.configure(state="normal")
        
        self.delete_inputs()
        
        self.username_entry.delete(0, "end")
        self.username_entry.insert(0, details[0])
        self.password_entry.delete(0, "end")
        self.password_entry.insert(0, details[1])
        self.role_entry.set(details[2])
        self.age_entry.delete(0, "end")
        self.age_entry.insert(0, details[3])
        self.gender_entry.delete(0, "end")
        self.gender_entry.insert(0, details[4])

    def add_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        role = self.role_entry.get()
        age = self.age_entry.get()
        gender = self.gender_entry.get()
        
        user_data = [username, password, role, age, gender]

        self.user_listbox.insert("end", " - ".join(user_data))
        
        with open("csv/users.csv", "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(user_data)
            
        tkmb.showinfo(title="User Created Successfully", message=f"You have successfully created {username}")
        self.delete_inputs()

    def edit_user(self):
        selected = self.user_listbox.curselection()
        
        if selected:
            username = self.username_entry.get()
            password = self.password_entry.get()
            role = self.role_entry.get()
            age = self.age_entry.get()
            gender = self.gender_entry.get()

            user_data = [username, password, role, age, gender]
            
            self.user_listbox.delete(selected)
            self.user_listbox.insert(selected, " - ".join(user_data))
            
            with open("csv/users.csv", "r") as file:
                lines = list(csv.reader(file))
                
            with open("csv/users.csv", "w", newline='') as file:
                writer = csv.writer(file)
                for i, line in enumerate(lines):
                    if i == (selected+1):
                        writer.writerow(user_data)
                    elif i != (selected+1):
                        writer.writerow(line)
                
            tkmb.showinfo(title="User Edited Successfully", message=f"You have successfully edited {username}")
            self.delete_inputs()

    def delete_user(self):
        selected = self.user_listbox.curselection()
        
        if selected:
            self.user_listbox.delete(selected)
            
            with open("csv/users.csv", "r") as file:
                lines = list(csv.reader(file))
                
            with open("csv/users.csv", "w", newline='') as file:
                writer = csv.writer(file)
                for i, line in enumerate(lines):
                    if i != (selected+1):
                        writer.writerow(line)
  
            tkmb.showinfo(title="User Deleted Successfully", message=f"You have successfully deleted {self.username_entry.get()}")
            self.delete_inputs()

    def type_change(self, choice):
        if choice == "Cinema":
            self.first_extra_label.configure(text="Movie Title:")
            self.second_extra_label.configure(text="Genre:")
        elif choice == "Sports":
            self.first_extra_label.configure(text="Sport Type:")
            self.second_extra_label.configure(text="Game Type:")
        elif choice == "Concert":
            self.first_extra_label.configure(text="Artist/Band:")
            self.second_extra_label.configure(text="Genre:")
        else:
            self.first_extra_label.config(text="Extra Info:")
            self.second_extra_label.configure(text="Extra Info:")

    def logout(self):
        self.destroy()

def run():
    ctk.set_appearance_mode("dark") 
    ctk.set_default_color_theme("blue")

    app = App()
    app.mainloop()