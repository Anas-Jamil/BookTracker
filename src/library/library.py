import json
import os
from . import manipulate  # Handles book-related functions
from . import user

class Library:
    def __init__(self):
        # File paths
        self.data_dir = os.path.join(os.path.dirname(__file__), '../data')
        self.users_file = os.path.join(self.data_dir, 'users.json')
        self.current_user = None

        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)

        self.users_data = {"allusers": []}
        if os.path.isfile(self.users_file):
            try:
                with open(self.users_file, 'r') as file:
                    self.users_data = json.load(file)
            except FileNotFoundError:
                # This case should be handled already
                pass
            except json.JSONDecodeError:
                print("Error decoding JSON from users file. Initializing empty data.")


    def view_books(self):
        if self.current_user and "library" in self.current_user and len(self.current_user["library"]) > 0:
            for book in self.current_user["library"]:
                print(f"ID: {book['id']}")
                print(f"Book: {book['title']}")
                print(f"Author: {book['author']}")
                print(f"Book Finished: {book['status']}")
                print(f"Page: {book['page']}")
                print('-' * 25)
        else:
            print("No books, consider adding one.\n")

    def add_book(self):
        manipulate.add_book(self.current_user)
        self.save_user_data()

    def delete_book(self):
        manipulate.delete_book(self.current_user)
        self.save_user_data()

    def change_status(self):
        manipulate.change_status(self.current_user)
        self.save_user_data()
    
    def save_user_data(self):
        with open(self.users_file, 'w') as file:
            json.dump(self.users_data, file, indent=4)

    def login(self):
        while True:
            print('Welcome to BookTrail!')
            print("1. Sign Up\n2. Sign In\n3. Exit")
            print("-" * 20)

            try:
                choose = int(input("Please select an option: "))
            except ValueError:
                print("Please enter an integer.")
                continue

            if choose == 1:
                self.sign_up()
            elif choose == 2:
                if self.sign_in():
                    self.option_select()  # Start the library options after sign-in
            elif choose == 3:
                print("Goodbye!")
                break
            else:
                print("Pick from the given menu!")
    
    def sign_up(self):
        user.sign_up(self)
        self.save_user_data()
    
    def sign_in(self):
        return user.sign_in(self)

    def option_select(self):
        while True:
            print(f'Welcome {self.current_user["email"]}!')
            print("Menu:\n1. View Current Library\n2. Add a Book\n3. Remove a Book\n4. Change Status\n5. Sign Out")
            print('-' * 20)
            
            try:
                choice = int(input('Please select an option: '))
            except ValueError:
                print("Invalid input! Please enter a number between 1 and 5.")
                continue  # Prompt the user again if the input is invalid
            
            if choice == 1:
                self.view_books()
            elif choice == 2:
                self.add_book()
            elif choice == 3:
                self.delete_book()
            elif choice == 4:
                self.change_status()
            elif choice == 5:
                print("Goodbye!")
                break
            else:
                print("Pick from the given menu!")
                
    # Attach the add_book, delete_book, change_status functions from manipulate.py
    add_book = manipulate.add_book
    delete_book = manipulate.delete_book
    change_status = manipulate.change_status
    sign_up = user.sign_up
    sign_in = user.sign_in

