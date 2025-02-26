import customtkinter as ctk
from PIL import Image
import tkinter.messagebox as tkmb 
import csv
import pandas as pd
import random
import string
from datetime import datetime
#PIL  Python Imaging Library. It provides support for opening, manipulating, and saving many different 
#image file formats. In this case, it's used to handle images for the GUI.

#The random module provides functions to generate random numbers, select random elements from lists, and 
#shuffle sequences. It's used to generate random IDs for transactions.

#The string module provides a collection of string constants and functions.
#It's used here  to generate random IDs by selecting characters from the alphabet.

#The datetime module provides classes for manipulating dates and times.
#It's used here to get the current date and time when recording transactions.


# Define a class named USER
class USER:
     # Initialize the class with master and username parameters
    def __init__(self, master, username, age, gender):
         # Assign the  parameters to the instance variables 
        self.master = master
        self.username = username
        self.age = age
        self.gender = gender
        
        #set title ,geometry,screen hieght and width for master window
        self.master.title("User")
        w, h = master.winfo_screenwidth(), master.winfo_screenheight()
        self.master.geometry("%dx%d+0+0" % (w, h))
        
        
        # Create the navigation bar frame
        self.task_bar_frame = ctk.CTkFrame(master, width=600, height=50,fg_color="#5B075D")
        self.task_bar_frame.grid(row=0, column=0, sticky="ew")


        # Create the content frame
        self.content_frame = ctk.CTkFrame(master, width=600, height=400,fg_color="#000000")
        self.content_frame.grid(row=1, column=0, sticky="nsew")
       

        # Configure grid weights
        self.task_bar_frame.grid_columnconfigure(4, weight=1)
        master.grid_rowconfigure(1, weight=1)
        master.grid_columnconfigure(0, weight=1)

        # Buttons on the navigation bar for different actions
        
        #main page-create_main_page_label()
        self.button1 = ctk.CTkButton(self.task_bar_frame, text="Book a Ticket", height=40,font=("Helvetica", 20,"bold"),fg_color="#5B075D",hover_color= "#460046", command=self.create_main_page_label)
        self.button1.grid(row=0, column=0, padx=10, pady=5)
        
        #My tickets-My_Tickets()
        self.button2 = ctk.CTkButton(self.task_bar_frame, text="My Tickets", height=40,font=("Helvetica", 20,"bold"),fg_color="#5B075D",hover_color= "#460046", command=lambda: self.My_Tickets(self.username))
        self.button2.grid(row=0, column=1, padx=10, pady=5)
        
        #log out function "not implemented yet"
        self.button3 = ctk.CTkButton(self.task_bar_frame, text="Logout", height=40,font=("Helvetica", 20,"bold"),fg_color="#5B075D", hover_color= "#460046", command=self.Logout)
        self.button3.grid(row=0, column=6, padx=10, pady=5)
        
        
        
    #creates the main page with images and three buttons to display cinema,concert and sport events .
    #The buttons associated with each event category trigger methods: cinema_events, sport_events, and concert_events,
    #passes the current username to fetch event data specific to the user.
    def create_main_page_label(self):
        self.clear_content_frame()
        label = ctk.CTkLabel(self.content_frame, text="Main Page")
        label.grid()
        
        self.content_frame.grid_rowconfigure(1, weight=1)
        self.content_frame.grid_columnconfigure(0, weight=1)
        
   
        fframe = ctk.CTkFrame(self.content_frame, width=600, height=50)
        fframe.grid(row=0, column=0, sticky="ew")
       
        sframe = ctk.CTkFrame(self.content_frame, width=600, height=350,fg_color="#000000")
        sframe.grid(row=1, column=0, sticky="nsew")
        
        # Configure the sframe to have three columns
        sframe.grid_columnconfigure(0, weight=1)
        sframe.grid_columnconfigure(1, weight=1)
        sframe.grid_columnconfigure(2, weight=1)
        
        my_image = ctk.CTkImage(light_image=Image.open('images/m2.jpg'),size=(1550,300))
        tlabel = ctk.CTkLabel(fframe, text="EVENTS",image=my_image,font=("Helvetica", 20, "bold"))
        tlabel.grid(row=0,column=0)
        
        my_image1 = ctk.CTkImage(light_image=Image.open('images/cinema2.png'),size=(255,250))
        i1label = ctk.CTkLabel(sframe, text="",image=my_image1)
        i1label.grid(row=1,column=0,pady=(50, 10))
        button1 = ctk.CTkButton(sframe, text="Cinema", fg_color="transparent",hover_color= "#5B075D",corner_radius=100,font=("Helvetica", 15, "bold"),command=lambda: self.cinema_events(self.username))
        button1.grid(row=2, column=0)
        
        my_image2 = ctk.CTkImage(light_image=Image.open('images/sport.png'),size=(250,250))
        i2tlabel = ctk.CTkLabel(sframe, text="",image=my_image2)
        i2tlabel.grid(row=1,column=1,pady=(50, 10))
        button3 = ctk.CTkButton(sframe, text="Sports Matches", fg_color="transparent",hover_color= "#5B075D",corner_radius=100,font=("Helvetica", 15, "bold"),command=lambda: self.sport_events(self.username))
        button3.grid(row=2, column=1)
        
        my_image3 = ctk.CTkImage(light_image=Image.open('images/concert.png'),size=(250,250))
        i3tlabel = ctk.CTkLabel(sframe, text="",image=my_image3)
        i3tlabel.grid(row=1,column=2, pady=(50, 10))
        button4 = ctk.CTkButton(sframe,text="Concerts",fg_color="transparent",hover_color= "#5B075D",corner_radius=100,font=("Helvetica", 15, "bold"),command=lambda: self.concert_events(self.username))
        button4.grid(row=2, column=2)
        
    
    #clears the content frame
    def clear_content_frame(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()
            
    #depending on the button pressed in the mainpage one of the bellow functions is called .
    #These methods fetches event data from event.csv file and passes it to the events method
    #along with the username and event category name .
    
    def cinema_events(self, username):
        filename = 'csv/CinemaEvent.csv'
        name="Movies"
        self.events(filename, username,name)
        
    def sport_events(self, username):
        filename = 'csv/SportsEvent.csv'
        name="Sports Games"
        self.events(filename, username,name)
        
    def concert_events(self, username):
        filename = 'csv/ConcertEvent.csv'
        name="Concerts"
        self.events(filename, username,name)
        
    #Displays events in the content frame based on the provided event data csv file, username, and event category name.
    def events(self, filename, username, name):
        #clears previous widgets
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        scrollbar_frame = ctk.CTkScrollableFrame(self.content_frame, width=600, height=350,fg_color="#000000",scrollbar_button_hover_color="#5B075D",scrollbar_button_color="#5B075D")
        scrollbar_frame.pack(fill="both", expand=True)  # Fill the entire root window
        
        #read csv file
        data = pd.read_csv(filename)
            
        titlelabel = ctk.CTkLabel(scrollbar_frame, text=name, justify="center", anchor="center", font=("Helvetica", 25, "bold"),fg_color="#000000")
        titlelabel.grid(row=0, column=0, columnspan=10, padx=5, pady=5)  # Span across 10 columns to center (2 empty on each side)
        
        row_counter = 1
        col_counter = 1  # Start from column 1 to center-align
    
        for i, row in data.iterrows():
            if col_counter > 6:  # Move to the next row after every 6 columns
                col_counter = 1
                row_counter += 1
            
            eframe = ctk.CTkFrame(scrollbar_frame,fg_color="#000000",border_color="#FFFFFF",border_width=3)  # Create eframe in scrollbar_frame
            eframe.grid(row=row_counter, column=col_counter, padx=20, pady=5, sticky="nsew")
            
            title_label = ctk.CTkLabel(eframe, text=row.iloc[5], justify="center", anchor="center", font=("Helvetica", 15, "bold"))
            title_label.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
            
            info_text = f"{row.iloc[2]}\n{row.iloc[6]} Duration:{row.iloc[7]}\nVenue:{row.iloc[4]}\nDate:{row.iloc[3]}\nVIP: ${row.iloc[9]}\nRegular: ${row.iloc[11]}"
            info_label = ctk.CTkLabel(eframe, text=info_text, justify="center", anchor="center", font=("Helvetica", 15))
            info_label.grid(row=1, column=0, padx=15, pady=5, sticky="nsew")
            
            #This lambda function calls the open_ticket_window method of the current object (self) 
            #with parameters r (the current row of data), data 
            #(the event data), filename (the filename of the CSV file), and username.
            choose_button = ctk.CTkButton(eframe,text="Choose",corner_radius=100,width=2,height=30,fg_color="black",hover_color="#FFFFFF",border_color="#FFFFFF",border_width=1,font=("Helvetica", 15, "bold"),  command=lambda r=row: self.open_ticket_window(r, data, filename, username))
            choose_button.grid(row=2, column=0, padx=30, pady=10, sticky="nsew")
            
            #functions to change button appearance on hover
            def on_enter(event, btn=choose_button):
                btn.configure(text_color="black",fg_color="#FFFFFF")
            def on_leave(event, btn=choose_button):
                btn.configure(text_color="white",fg_color="black")
            choose_button.bind("<Enter>", on_enter)
            choose_button.bind("<Leave>", on_leave)

            col_counter += 1
    
         #Configure grid columns to ensure centering
        scrollbar_frame.grid_columnconfigure(0, weight=1)
        scrollbar_frame.grid_columnconfigure(9, weight=1)
    
        return
   
    #Opens a ticket selection window for the specified event
    #calculate _button calls the calculate_price function to check availability of the chosen tickets 
    #pay_Button is disabeld until the selected tickets have been confirmed to be available and is activated in the calculate_price()
    #when activated calls function pay()
    #cancel_button calls a function that clears the open ticket widow 
    def open_ticket_window(self,row,data,filename,username):
        ticket_window = ctk.CTk()
        ticket_window.title("Ticket Selection")
        ticket_type_var = ctk.StringVar(ticket_window)
        ticket_window.configure(fg_color="#000000") 
        ticket_window.geometry("300x330")
        
        ticket_type_var.set("VIP")  # Set default selection to "VIP"
        ctk.CTkRadioButton(ticket_window, text="VIP Ticket",font=("Helvetica",15) ,variable=ticket_type_var, value="VIP",fg_color="#5B075D",hover_color="#5B075D").pack(pady=(20,5))
        ctk.CTkRadioButton(ticket_window, text="Regular Ticket",font=("Helvetica",15), variable=ticket_type_var, value="Regular",fg_color="#5B075D",hover_color="#5B075D").pack(pady=5)
        
        num_tickets_var = ctk.StringVar(ticket_window)
        num_tickets_var.set("1")  
        combobox = ctk.CTkComboBox(ticket_window, values=[str(i) for i in range(1, 13)], variable=num_tickets_var,fg_color="#5B075D")
        combobox.pack(padx=20, pady=10)
        
        price_label = ctk.CTkLabel(ticket_window,text="")
        price_label.pack()
        
        # Button to calculate ticket price
        calculate_button = ctk.CTkButton(ticket_window, text="Check tickets availability",text_color="white",corner_radius=100,width=2,height=30,fg_color="black",hover_color="#5B075D",border_color="#FFFFFF",border_width=1,font=("Helvetica", 15, "bold"), command=lambda: self.calculate_price(row, ticket_type_var.get(), num_tickets_var.get(), ticket_window, price_label, pay_button))
        calculate_button.pack(pady=10)
        
        #Pay
        pay_button = ctk.CTkButton(ticket_window, text="Proceed to Payment", text_color="white",state=ctk.DISABLED, corner_radius=100,width=2,height=30,hover_color="#5B075D",fg_color="black",border_color="#FFFFFF",border_width=1,font=("Helvetica", 15, "bold"),command=lambda:self.pay(row, ticket_type_var.get(), num_tickets_var.get(),data,filename,ticket_window,username))
        pay_button.pack(pady=10)
        
        # Button to cancel ticket selection
        cancel_button = ctk.CTkButton(ticket_window, text="Cancel",text_color="white",corner_radius=100,width=2,height=30,fg_color="black",hover_color="#5B075D",border_color="#FFFFFF",border_width=1,font=("Helvetica", 15, "bold"), command=ticket_window.destroy)
        cancel_button.pack(pady=10)
       
        ticket_window.mainloop()
        
        
        
    #check ticket availability based on the chosen type and diplays a text in the price_label in open ticket window 
    #in case tickkets are sold out or not available in the requested quantity 
    #if the tickets are available the price will be displayed and the pay button will be activated in the open ticket window
    def calculate_price(self,row, ticket_type_var, num_tickets_var, ticket_window, price_label, pay_button):
        num_tickets_var = int(num_tickets_var)
        VIPprice= row['VIP_ticket_price']
        REGprice= row['Regular_ticket_price']
        VIPtickets_available=(row['VIP_tickets_available'])
        Regulartickets_available=(row['Regular_tickets_available'])
        
        if ticket_type_var == "VIP":
            if VIPtickets_available==0:
                price_label.configure(text="Tickets sold out",font=("Helvetica",15))
                pay_button.configure(state=ctk.DISABLED)
                return
            if VIPtickets_available<num_tickets_var:
                    price_label.configure(text=f"There are only {VIPtickets_available} tickets available",font=("Helvetica",15))
                    pay_button.configure(state=ctk.DISABLED)
                    return  # Exit the function if no tickets enough are available
            if VIPtickets_available > 0 :
                    price=(VIPprice)*num_tickets_var
                    price_label.configure(text=f"Price: {price}$",font=("Helvetica",15))  # Update label with price
                    pay_button.configure(state=ctk.NORMAL)
                    return
                
        elif ticket_type_var == "Regular":
            if Regulartickets_available==0:
                price_label.configure(text="Tickets sold out",font=("Helvetica",15))
                pay_button.configure(state=ctk.DISABLED)
                return
            if Regulartickets_available<num_tickets_var:
                    price_label.configure(text=f"There are only {ticket_type_var} tickets available",font=("Helvetica",15))
                    pay_button.configure(state=ctk.DISABLED)
                    return  # Exit the function if no tickets enough are available
            if Regulartickets_available > 0 :
                    price=(REGprice)*num_tickets_var
                    price_label.configure(text=f"Price: {price}$",font=("Helvetica",15))  # Update label with price
                    pay_button.configure(state=ctk.NORMAL)
                    return
            return
   

   #proceeds the payment procces of the selected tickets
    #defines variables(column name of the selected ticket and its type and price)
    #creates a credit card form with a pay and cancel button ,the entries and comboboxes are all validated and display error
    #messages for each condition
    #after validation is true the pay_button_clicked function displays a"Payment successful" message and updates the number of 
    #tickets available deducting the bokked tickets based on the selected ticket type and numbers of tickets 
    #calls function record_transcation() and create_main_page _label to get back to main page
    def pay(self,row, ticket_type_var, num_tickets_var,data,filename,ticket_window,username):
        ticket_window.destroy()
        self.clear_content_frame()
        if ticket_type_var == "VIP":
            column_name = 'VIP_tickets_available'
            T_type="VIP"
            price=row['VIP_ticket_price']*int(num_tickets_var)
            
        elif ticket_type_var == "Regular":
            column_name = 'Regular_tickets_available'
            T_type="Regular"
            price=row['Regular_ticket_price']*int(num_tickets_var)
            
        def validate_inputs():
            card_number = card_number_entry.get()
            card_holder = card_holder_entry.get()
            month = month_combobox.get()
            year = year_combobox.get()
            csv = csv_entry.get()
        
            # Validation 1: Check if card number has 16 characters and they are integers
            if len(card_number) != 16 or not card_number.isdigit():
                tkmb.showerror("Error", "Card number must be a 16-digit integer.")
                return False
            
            # Validation 2: Check if CVV has 3 characters and they are integers
            if len(csv) != 3 or not csv.isdigit():
                tkmb.showerror("Error", "CVV must be a 3-digit integer.")
                return False
            
            # Validation 3: Check if card holder contains only alphabetical characters and at most one space
            if not card_holder.replace(' ', '').isalpha() or card_holder.count(' ') > 1:
                tkmb.showerror("Error", "Card holder must contain only alphabetical characters .")
                return False
            
            # Validation 4: Check if month and year have been selected
            if month == "Month" or year == "Year":
                tkmb.showerror("Error", "Please select a month and year.")
                
                return False
            
            return True
        
        def pay_button_clicked():
            if validate_inputs():
                tkmb.showinfo("Success", "Payment successful!")  
                 # Get the index of the row to update
                index = row.name
                # Get the current value of tickets available
                tickets_available = data.loc[index, column_name]
                # Calculate the updated number of tickets available
                tickets_update = tickets_available - int(num_tickets_var)
                # Update the DataFrame with the new value
                data.at[index, column_name] = tickets_update
                # Write the updated DataFrame back to the CSV file
                data.to_csv(filename, index=False)
                self.record_transaction(row,num_tickets_var,T_type,username,price)
                self.create_main_page_label()
        
       
        
        # Create the content frame
        content_frame = ctk.CTkFrame(self.content_frame, width=800, height=400)
        content_frame.place(relx=0.5, rely=0.5, anchor="center")
        
        # Create the credit frame inside the content frame
        credit_frame = ctk.CTkFrame(content_frame, width=800, height=400, fg_color="#5B075D")
        credit_frame.grid(row=0, column=0, padx=20, pady=20)
        
        # Configure the grid layout
        credit_frame.grid_columnconfigure(0, weight=1)
        credit_frame.grid_columnconfigure(1, weight=1)
        
        # Load an image 
        image = ctk.CTkImage(light_image=Image.open('images/cc5.png'), size=(350, 250))
        
        # Create and place the image label in the first column
        image_label = ctk.CTkLabel(credit_frame, image=image, text=f"Total: {price}$",compound="bottom",font=("Helvetica", 20, "bold"))
        image_label.grid(row=1, column=0, padx=10, pady=15, rowspan=7)
        
        # Create and place the entry for card number in the second column
        card_number_entry = ctk.CTkEntry(credit_frame, placeholder_text="Card Number", fg_color="#000000")
        card_number_entry.grid(row=1, column=1, padx=10, pady=10, sticky="ew")
        
        # Create and place the entry for card holder in the second column
        card_holder_entry = ctk.CTkEntry(credit_frame, placeholder_text="Card Holder", fg_color="#000000")
        card_holder_entry.grid(row=2, column=1, padx=10, pady=10, sticky="ew")
        
        # Create and place the expiry date label in the second column
        expiry_date_label = ctk.CTkLabel(credit_frame, text="Expiry Date", font=("Helvetica", 15, "bold"))
        expiry_date_label.grid(row=3, column=1, padx=10, pady=(10, 0), sticky="w")
        
        # Create a frame to hold the comboboxes
        expiry_date_frame = ctk.CTkFrame(credit_frame, fg_color="#5B075D")
        expiry_date_frame.grid(row=4, column=1, padx=10, pady=10, sticky="ew")
        
        # Create and place the combobox for the month in the expiry date frame
        month_combobox = ctk.CTkComboBox(expiry_date_frame, values=[f"{i:02d}" for i in range(1, 13)], fg_color="#000000")
        month_combobox.set("Month")
        month_combobox.grid(row=0, column=0, padx=5, pady=10)
        
        # Create and place the combobox for the year in the expiry date frame
        year_combobox = ctk.CTkComboBox(expiry_date_frame, values=[str(i) for i in range(2023, 2033)], fg_color="#000000")
        year_combobox.set("Year")
        year_combobox.grid(row=0, column=1, padx=5, pady=10)
        
        # Create and place the entry for the CSV in the second column
        csv_entry = ctk.CTkEntry(credit_frame, placeholder_text="CSV", fg_color="#000000")
        csv_entry.grid(row=5, column=1, padx=10, pady=10, sticky="ew")
        
        # Create a frame to hold the buttons
        button_frame = ctk.CTkFrame(credit_frame, fg_color="#5B075D")
        button_frame.grid(row=6, column=1, padx=10, pady=10, sticky="ew")
        
        # Create and place the Pay button in the button frame
        pay_button = ctk.CTkButton(button_frame, text="Pay", text_color="white", corner_radius=100, height=30, fg_color="#5B075D", hover_color="black", border_color="#FFFFFF", border_width=1, font=("Helvetica", 15, "bold"), command=pay_button_clicked)
        pay_button.grid(row=0, column=0, padx=5)
        
        # Create and place the Cancel button in the button frame
        cancel_button = ctk.CTkButton(button_frame, text="Cancel", text_color="white", corner_radius=100, height=30, fg_color="#5B075D", hover_color="black", border_color="#FFFFFF", border_width=1, font=("Helvetica", 15, "bold"), command=self.create_main_page_label)
        cancel_button.grid(row=0, column=1, padx=5)
        
        # Create and place the label for Credit Card Payment
        payment_label = ctk.CTkLabel(credit_frame, text="Credit Card Payment", font=("Helvetica", 20, "bold"), fg_color="#5B075D")
        payment_label.grid(row=0, column=0, columnspan=2, pady=(20, 10), sticky="n")
           
        return  
    
    #records the transaction details of a ticket purchase
    #This method generates a unique transaction ID, records the transaction date, ticket type, number of tickets,
    #price, event details, and user information into a CSV file named "csv/transactions.csv"
    #datetime.now() is  function from the datetime module returns a datetime object representing the current date and time.
    #strftime("%Y-%m-%d") formats the datetime object into a string according to the specified format string. 
    ###recording the user info (age and gender) is still missing###

    def record_transaction(self,row,num_tickets_var,T_type,username,price):
        
        # Function to generate a random ID
        def generate_random_id():
            letters = ''.join(random.choices(string.ascii_uppercase, k=2))
            numbers = ''.join(random.choices(string.digits, k=4))
            return letters + numbers
        
        df = pd.read_csv('csv/transactions.csv')

        # Generate a new unique ID 
        new_id = generate_random_id()
        
        # Check if the generated ID already exists in the first column
        while new_id in df.iloc[:, 0].values:
            new_id = generate_random_id()
            
         # Get today's date
        today_date = datetime.now().strftime("%Y-%m-%d")
         
         # Read the CSV file and append transcation data in transcations.csv
        new_row = pd.DataFrame([[new_id,row.iloc[1] ,today_date ,username, T_type,num_tickets_var,price,row.iloc[0],row.iloc[5],row.iloc[2],row.iloc[6],row.iloc[3],row.iloc[7],row.iloc[4], self.age, self.gender]],
                               columns=[df.columns[0],'Event ID','Purchase Date', 'T_Type','username', 'Num_Tickets','Purchase','Event','Details','Name','Genre','EventDate','Duration','Venue','Age','Gender']) 
        new_row.to_csv('csv/transactions.csv',mode='a', header=False,index=False)
        return
           

   #Displays tickets booked by the given username.filters the transaction.csv based on the username
    #Button to cancel the booking .call the cancel_booking() function
    def My_Tickets(self, username):
        
        self.clear_content_frame()
        
        
        # Create a scrollable frame to display tickets
        scrollbar_frame = ctk.CTkScrollableFrame(self.content_frame, width=600, height=350,fg_color="#000000",scrollbar_button_hover_color="#5B075D",scrollbar_button_color="#5B075D")
        scrollbar_frame.pack(fill="both", expand=True)  # Fill the entire root window
        
        label = ctk.CTkLabel(scrollbar_frame, text="My Tickets", font=("Helvetica", 20, "bold"))
        label.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")
        
        data = pd.read_csv("csv/transactions.csv")
        
        row_counter = 1
        col_counter = 1  # Start from column 1 to center-align
        s=0  # Counter for displaying ticket number
        
         # Iterate over each ticket transaction
        for i, trow in data.iterrows():
            if trow['Username'] == username:# Check if the ticket belongs to the specified username
                
                # Create a frame for displaying ticket details
                eframe = ctk.CTkFrame(scrollbar_frame,fg_color="#000000",border_color="#FFFFFF",border_width=3)  # Create eframe in self.content_frame
                eframe.grid(row=row_counter, column=col_counter, padx=30, pady=30, sticky="nsew")
                s+=1# Increment ticket number counter
                
                # Label for indicating ticket number
                title_label = ctk.CTkLabel(eframe, text=f"Ticket {s}", justify="center", anchor="center", font=("Helvetica", 20, "bold"))
                title_label.grid(row=0, column=0, padx=50, pady=5, sticky="nsew")
            
                #display ticket info
                ticket_info = f"Transaction ID: {trow['Tra_ID']}      Event: {trow['Event']}      Purchase Date: {trow['Purchase Date']}\nDetails:  {trow['Details']}      {trow['Name']}      {trow['Genre']}  \nEvent Date: {trow['Duration']}       Duration: {trow['Duration']}      Venue: {trow['Venue']}\n Tickets booked: {trow['T_type']}    {trow['Num_Tickets']}    Purchase: {trow['Purchase']}$"                
                info_label = ctk.CTkLabel(eframe, text=ticket_info, font=("Helvetica", 15))
                info_label.grid(row=1, column=0, padx=50)
                
                # Button to cancel the booking .call the cancel_booking() function
                delete_button = ctk.CTkButton(eframe, text="Cancel Booking",corner_radius=100,text_color="white",width=2,height=30,fg_color="black",hover_color="#DB2C2C",border_color="#FFFFFF",border_width=2,font=("Helvetica", 15, "bold"), command=lambda idx=i: self.cancel_booking(idx, username))
                delete_button.grid(row=2, column=0, padx=5, pady=15)
                
                # Increment column counter, and reset it and increment row counter after every two frames
                col_counter += 1
                if col_counter > 2:  # Move to next row after two columns
                    col_counter = 1
                    row_counter += 1
    
        # Configure grid columns to ensure centering
        scrollbar_frame.grid_columnconfigure(0, weight=1)
        scrollbar_frame.grid_columnconfigure(3, weight=1)
    
        return
    
    
    
    #Cancels a booking for a specific ticket transaction and updates the ticket availability for the corresponding event.
    def cancel_booking(self,idx,username):
        
        #read transaction file
        data = pd.read_csv("csv/transactions.csv")
        
        #necessary information from the ticket transaction 
        #idx (int) is the index of the row  of the ticket transaction to be canceled.
        Event=data.loc[idx, 'Event']
        E_ID=data.loc[idx, 'Event ID']
        T_type=data.loc[idx, 'T_type']
        T_num=data.loc[idx, 'Num_Tickets']
        
     
    
        # Drop the row at the specified index
        data = data.drop(idx)
        # Save the updated DataFrame back to the CSV file
        data.to_csv("csv/transactions.csv", index=False)
        
        
        # Refresh the tickets display
        self.My_Tickets(username)
        
         #Add tickets back to the event to be available for booking
        
        #based on the event name a file is assigned to filename variable
        if Event == "SportsEvent":
            file_name = "csv/SportsEvent.csv"
        elif Event == "CinemaEvent":
            file_name = "csv/CinemaEvent.csv"
        elif Event == "ConcertEvent":
            file_name = "csv/ConcertEvent.csv"
            
            
        #the file is read 
        if file_name:
            df = pd.read_csv(file_name)
            # Iterate over each row in the event data
            for i, row in df.iterrows():
                 # Find the event matching the canceled ticket based on the Event ID
                if row['Event_ID'] == E_ID:
                     # Increment the ticket availability based on the ticket type
                    if T_type=='VIP':
                        df.at[i, 'VIP_tickets_available'] = row['VIP_tickets_available'] + T_num
                    if T_type=="Regular":
                        df.at[i, 'Regular_tickets_available'] = row['Regular_tickets_available'] + T_num

           # Update the event data in the CSV file
            df.to_csv(file_name, index=False)
    
    ###function unimplemented yet###
    def Logout(self):
        self.master.destroy()
        
#Creates an instance of the USER class, initializes the main page label, and starts the main event loop.

def run(root, username, age, gender):
    # Create the root Tkinter window
    app = USER(root, username, age, gender)
    app.create_main_page_label()
    root.mainloop()