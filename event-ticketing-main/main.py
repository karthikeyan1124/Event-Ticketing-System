import csv
import customtkinter as ctk
import tkinter.messagebox as tkmb
import admin, user

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class LoginPage:
    def __init__(self, master):
        self.master = master
        self.master.geometry("500x500")
        self.master.title("Events Ticketing System")

        self.frame = ctk.CTkFrame(master=self.master)
        self.frame.pack(pady=20, padx=40, fill="both", expand=True)

        self.login_widgets()

    def verify(self, username, password):
        with open("csv/users.csv", mode='r', newline='') as file:
            reader = csv.reader(file)
            rows = list(reader)

            for row in rows:
                if row[0] == username.get().lower():
                    if row[1] == password.get():
                        tkmb.showinfo(title="Login Successful", message="You have logged in Successfully")
                        if row[2] == "admin":
                            return self.admin_page()
                        else:
                            return self.main_page(username.get(), row[3], row[4])
                    else:
                        password.configure(text_color="red")
                        return tkmb.showerror(title="Login Failed", message="Incorrect password")

        return tkmb.showerror(title="Login Failed", message="Invalid username or password")

    def signup(self, username, password, age, gender):
        if password.get() == "" or username.get() == "":
            return tkmb.showerror(title="Signup Failed", message="Please fill in all the fields")

        with open("csv/users.csv", "r+", newline='') as file:
            reader = csv.reader(file)
            rows = list(reader)

            for row in rows:
                if username.get().lower() == row[0]:
                    return tkmb.showerror(title="Signup Failed", message="This username already exists. Please login")

            writer = csv.writer(file)
            writer.writerow([username.get().lower(), password.get(), 'user', age.get(), gender.get()])
            tkmb.showinfo(title="Signup Successful", message="You have signed up Successfully")
            return self.main_page(username.get().lower())

    def signup_widgets(self):
        # Destroy all existing widgets in the frame
        for widget in self.frame.winfo_children():
            widget.destroy()

        label = ctk.CTkLabel(master=self.frame, text="Signup", font=("Arial", 40))
        label.pack(pady=12, padx=10)

        username = ctk.CTkEntry(master=self.frame, placeholder_text="Username", font=("Arial", 17), width=200)
        username.pack(pady=(20, 5), padx=10)

        password = ctk.CTkEntry(master=self.frame, placeholder_text="Password", show="*", font=("Arial", 17), width=200)
        password.pack(pady=5, padx=10)
        
        age = ctk.CTkEntry(master=self.frame, placeholder_text="Age", font=("Arial", 17), width=200)
        age.pack(pady=5, padx=10)
        
        gender = ctk.CTkEntry(master=self.frame, placeholder_text="Gender", font=("Arial", 17), width=200)
        gender.pack(pady=5, padx=10)

        signup_button = ctk.CTkButton(master=self.frame, text="Signup", command=lambda: self.signup(username, password, age, gender), font=("Arial", 20), width=200)
        signup_button.pack(pady=(15,5), padx=10)

        login_button = ctk.CTkButton(master=self.frame, text="Login", command=self.login_widgets, font=("Arial", 17), width=200)
        login_button.pack(pady=5, padx=10)

    def login_widgets(self):
        # Destroy all existing widgets in the frame
        for widget in self.frame.winfo_children():
            widget.destroy()

        label = ctk.CTkLabel(master=self.frame, text="Login", font=("Arial", 40))
        label.pack(pady=12, padx=10)

        username = ctk.CTkEntry(master=self.frame, placeholder_text="Username", font=("Arial", 17), width=200)
        username.pack(pady=(20, 5), padx=10)

        password = ctk.CTkEntry(master=self.frame, placeholder_text="Password", show="*", font=("Arial", 17), width=200)
        password.pack(pady=5, padx=10)

        login_button = ctk.CTkButton(master=self.frame, text="Login", command=lambda: self.verify(username, password), font=("Arial", 20), width=200)
        login_button.pack(pady=(15,5), padx=10)

        signup_button = ctk.CTkButton(master=self.frame, text="Signup", command=self.signup_widgets, font=("Arial", 17), width=200)
        signup_button.pack(pady=5, padx=10)

    def main_page(self, username, age, gender):
        self.master.destroy()
        user.run(ctk.CTk(), username, age, gender)

    def admin_page(self):
        self.master.destroy()
        admin.run()

if __name__ == "__main__":
    app = ctk.CTk()
    login_page = LoginPage(app)
    app.mainloop()
