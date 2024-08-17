# BookTrail

## Overview

**BookTrail** is a comprehensive book tracking application designed to help users manage their reading lists efficiently. Built with Python, it offers functionalities for adding, viewing, removing, and updating books in a personal library. The application leverages secure user authentication and stores data in JSON format, ensuring that users' information and reading history are well-managed.

## Features

- **User Authentication**: Secure sign-up and sign-in features using hashed passwords with bcrypt.
- **Personalized Library**: Users can add books, track their reading progress, and update book statuses.
- **Book Management**: Includes options to view, add, delete, and change the status of books.
- **Data Persistence**: User data and book information are stored in a JSON file, which is updated dynamically based on user interactions.
- **Error Handling**: Robust validation for user inputs and file operations to ensure smooth operation and a user-friendly experience.

## Key Components

- **Library Class**: Manages user interactions, book operations, and data persistence.
- **Manipulate Module**: Contains functions for adding, deleting, and updating books in the user's library.
- **User Module**: Handles user authentication, including sign-up and sign-in processes.
- **users.json**: Stores user data and book information in a structured JSON format.

## Requirements

- Python 3.x
- `bcrypt` library for password hashing
- `json` module for data handling

## Installation

### Step 1: Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/Anas-Jamil/BookTracker.git
cd File-Organizer-
```

### Step 2: Ensure Python is Installed
Make sure Python 3.x is installed on your system. You can check by running:
```bash
python --version
```

### Step 3: Install Requirements
Install the required libraries:
```bash
pip install requirements.txt
```

## Usage

### Step 1: Run the Application
Navigate to the project directory and run the application:
```bash
python main.py
```

### Step 2: Follow the Prompts
The application will guide you through signing up or signing in, and then you can use the menu options to manage your book library.

## Future Plans

**BookTrail** is currently a console-based application. Future plans include transforming it into a deployable web application to enhance user accessibility and interaction. The web version will feature:

- **Web Interface**: A user-friendly web interface for managing books and user accounts.
- **Enhanced Security**: Advanced security features for user authentication and data protection.
- **Scalability**: Improved data management with a robust backend and database integration.


## Contributing
If you want to contribute to this project, feel free to fork the repository and submit a pull request. Contributions such as bug fixes, new features, and documentation improvements are welcome.
