import json
import bcrypt

def sign_up(library):
    while True:
        email = input("Please enter your email: ").strip().lower()
        
        # Validate email format
        if "@" not in email or "." not in email:
            print("Please enter a valid email address.")
            continue

        # Check if email already exists
        email_exists = any(user["email"] == email for user in library.users_data["allusers"])
        if email_exists:
            print("The email already exists, consider signing in.")
            return
        
        break

    while True:
        password = input("Please enter a password: ")
        
        # Validate password length
        if len(password) > 30:
            print("Password is too long.")
        elif len(password) < 5:
            print("Password is too short.")
        elif not any(char.isupper() for char in password):
            print("Please have at least one capital letter.")
        else:
            break

    # Hash the password before storing
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    # Create new user
    new_user = {
        "email": email,
        "password": hashed_password.decode('utf-8'),
        "library": []
    }

    # Add new user to the list and save data
    library.users_data["allusers"].append(new_user)
    with open(library.users_file, 'w') as file:
        json.dump(library.users_data, file, indent=4)

    print("You have successfully signed up!")

def sign_in(library):
    email = input("Please enter your email: ").strip().lower()
    
    # Find the user by email
    user_found = next((user for user in library.users_data["allusers"] if user["email"] == email), None)
    
    if not user_found:
        print("This email does not exist.")
        return False
    
    while True:
        password = input("Please enter your password: ")
        hashed_password = user_found["password"].encode('utf-8')
        
        # Verify password
        if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
            print("Hello! You have successfully signed in.")
            library.current_user = user_found
            return True
        else:
            print("Incorrect password. Please try again.")
