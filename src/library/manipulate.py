import json

def add_book(self):
    book_count = 0  # Initialize book count to 0

    # 20-31, Take user input, check if the book already exists, if not then insert it into the user's library
    while True:
        book_name = input('Please enter the book name: ')   # User Input  
        book_exists = False

        for book in self.current_user["library"]:
            if book["title"].lower() == book_name.lower():
                print('The book already exists')
                book_exists = True
                break
        if not book_exists:
            break

    author_name = input('Please enter the author: ')  # User Input

    while True: 
        stat = input('Is the book completed (Yes/No): ').strip().lower()
        if stat == 'yes':
            status = True
            break
        elif stat == 'no':
            status = False
            break
        else:
            print("Please enter yes or no only!")
    
    while True: 
        try:
            pages = int(input("What is your current page: "))
            if pages < 0:
                raise ValueError("Cannot have negative pages")
            else: 
                break
        except ValueError:
            print("Please enter an integer only")
            
    # 21-24, If the user's library is non-empty, set the book count variable to the ID of the last element + 1
    if self.current_user["library"]:
        book_count = self.current_user["library"][-1]["id"] + 1
    else:
        book_count = 1

    # 27-33, New input field to then append to the user's library
    new_book = {
        "id": book_count,
        "title": book_name,
        "author": author_name,
        "status": status,
        "page": pages
    }

    self.current_user["library"].append(new_book)

    # Save the updated user data back to the JSON file
    self.save_user_data()

def delete_book(self):
    self.view_books()
    if len(self.current_user["library"]) > 0:
        while True:
            try:
                del_select = int(input('Please enter the ID of the book to remove: '))
                if del_select > self.current_user["library"][-1]["id"] or del_select < 0:
                    print('Please select an appropriate value')
                else:
                    break
            except ValueError:
                print('Please enter a valid integer')

        self.current_user["library"] = [book for book in self.current_user["library"] if book["id"] != del_select]

        # Update the ID of the remaining books if applicable
        if len(self.current_user["library"]) > 0:
            for i, book in enumerate(self.current_user["library"]):
                book["id"] = i + 1

        # Save the updated user data back to the JSON file
        self.save_user_data()

        print(f'Book with ID {del_select} has been removed.')
    else:
        print("No books available to remove.")

def change_status(self):
    if len(self.current_user["library"]) > 0:
        while True:
            try:
                edit = int(input('Please enter the ID of the book to edit: '))
                if edit > self.current_user["library"][-1]["id"] or edit < 0:
                    print('Please select an appropriate value')
                else:
                    break
            except ValueError:
                print('Please enter a valid integer')
        
        selection = None
        for i, book in enumerate(self.current_user["library"]):
            if book["id"] == edit:
                selection = i
                break

        if selection is not None:
            while True: 
                choiceFinish = input('Is the book completed (Yes/No): ').strip().lower()
                if choiceFinish == 'yes':
                    status = True
                    break
                elif choiceFinish == 'no':
                    status = False
                    break
                else:
                    print("Please enter yes or no only!")
            
            while True: 
                try:
                    pages = int(input("What is your current page: "))
                    if pages < 0:
                        raise ValueError("Cannot have negative pages")
                    else: 
                        break
                except ValueError:
                    print("Please enter an integer only")
            
            # Update the book's status and page
            self.current_user["library"][selection]["status"] = status
            self.current_user["library"][selection]["page"] = pages
            
            # Save the updated user data back to the JSON file
            self.save_user_data()

            print(f"Book ID {edit} has been updated.")
        else:
            print("Book ID not found.")
    else:
        print("No books available to edit.")
