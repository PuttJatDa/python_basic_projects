# Python Basic Projects

This repository contains a collection of basic Python projects designed to practice Python programming. Each project focuses on different aspects of Python, from basic syntax to more complex functionalities.

## Project 2: Library Management System

### Overview

The Library Management System is a Python-based application that allows users to manage book loans in a library. The system supports adding new books, loaning out books to users, returning books, and saving/loading data from CSV files.

### Features

- **Add New Books**: Add new books to the library's inventory.
- **Loan Books**: Loan out books to users and update their availability status.
- **Return Books**: Return books and update the records.
- **Data Persistence**: Save and load library data from CSV files.


### Usage

1. **Run the main script:**

    ```bash
    python main.py
    ```

2. **Follow the prompts:**

    - **Enter your name**: The system will check if you are a registered user. If not, it will create a new user record for you.
    - **Choose an action**: You can choose to Loan a book, Return a book, Add a new book, or Exit the system.

### Example Interaction

#### 1. Starting the Program

```bash
python main.py
2. User Login or Registration
Plain text
Enter your name: alice
If alice is not in the users' CSV, the system will create a new user record for alice.
3. Choosing an Action
Plain text
Please enter what you want to do (Loan, Return, Add, Exit): loan
Actions Explained
Loan a Book
Prompt: Hey alice, please enter the title of the book:
Example: book_title1
Outcome:
If the book is available, it will be loaned to alice, and the book's availability status will be updated.
If the book is not available, the system will inform alice that the book is already loaned out.
Return a Book
Prompt: Hey alice, please enter the title of the book:
Example: book_title1
Outcome:
If alice has borrowed the book, it will be returned, and the book's availability status will be updated.
If alice has not borrowed the book, the system will inform her.
Add a New Book
Prompt: Enter book name:
Example: new_book_title
Prompt: Please enter the author of new_book_title:
Example: new_author_name
Outcome:
If the book is not already in the library, it will be added to the inventory.
If the book is already present, the system will inform alice.
Exit
Outcome:
The system will save the current state of the library and user data to the CSV files and exit the program.
File Structure
main.py: The main script to run the library management system.
books.csv: CSV file to store book details.
users.csv: CSV file to store user details.
Example CSV Files
books.csv
Book ID	Title	Author	Available?	Borrower
B_001	book_title1	author_name1	Yes	
B_002	book_title2	author_name2	No	user1
users.csv
User ID	Name	Borrowed Books
U_001	user1	book_title2
U_002	user2	
Contributing
Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes.
Commit your changes (git commit -m 'Add some feature').
Push to the branch (git push origin feature-branch).
Open a pull request.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Contact
If you have any questions or suggestions, feel free to open an issue or contact me at [your-email@example.com].