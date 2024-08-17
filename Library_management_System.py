import csv

# Define the Book class to represent each book in the library
class Book:
    def __init__(self, title, book_details):
        # Initialize book attributes
        self.book_id = book_details[0]  # Unique identifier for the book
        self.title = title  # Title of the book
        self.author = book_details[2]  # Author of the book
        self.is_available = book_details[3]  # Availability status of the book
        self.borrower = book_details[4]  # Name of the borrower if the book is loaned out

    def get_all_values(self):
        # Return all book details as a list
        return [self.book_id, self.title, self.author, self.is_available, self.borrower]

# Define the User class to represent each user in the library system
class User:
    def __init__(self, user_name, user_details):
        # Initialize user attributes
        self.user_id = user_details[0]  # Unique identifier for the user
        self.user_name = user_name  # Name of the user
        self.borrowed_books = user_details[2]  # List of books borrowed by the user

    def get_all_values(self):
        # Return all user details as a list
        return [self.user_id, self.user_name, self.borrowed_books]

# Function to read books or users from a CSV file and return a dictionary of objects
def read_csv_file(file_path, class_type):
    items = {}
    try:
        with open(file_path, "r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                key = row[1].lower()  # Use the title (for books) or name (for users) as the key
                items[key] = class_type(row[1], row)  # Create an instance of the class and add to dictionary
    except FileNotFoundError:
        print(f"No record found at {file_path}.")
    return items

# Function to write books or users to a CSV file
def write_csv_file(file_path, column_names, items):
    print("Writing the files")
    with open(file_path, 'w', newline='') as writefile:
        writer = csv.writer(writefile)
        writer.writerow(column_names)  # Write the header row
        for item in items.values():
            writer.writerow(item.get_all_values())  # Write each item's details

# Function to loan out a book to a user
def loan_out_book(books, users, title, user_name):
    title = title.lower()  # Convert title to lowercase for consistency
    user_name = user_name.lower()  # Convert user name to lowercase for consistency
    if title in books:
        if books[title].is_available == "Yes":
            books[title].is_available = "No"  # Mark book as not available
            books[title].borrower = user_name  # Record the borrower
            if users[user_name].borrowed_books == '':
                users[user_name].borrowed_books = title  # Add book to user's borrowed list
            else:
                users[user_name].borrowed_books += f",{title}"  # Append book to user's borrowed list
        else:
            print(f"Sorry, but {title} is already loaned out by another user. Please try another book.")
    else:
        print(f"{title} not found in the library.")

# Function to return a book from a user
def return_book(books, users, title, user_name):
    title = title.lower()  # Convert title to lowercase for consistency
    user_name = user_name.lower()  # Convert user name to lowercase for consistency
    if title in books:
        borrowed_books = users[user_name].borrowed_books.split(',')  # Split borrowed books into a list
        borrowed_books = [book.lower() for book in borrowed_books]  # Convert all titles to lowercase
        if title in borrowed_books:
            borrowed_books.remove(title)  # Remove the returned book from the list
            users[user_name].borrowed_books = ','.join(borrowed_books)  # Update the user's borrowed books list
            books[title].is_available = "Yes"  # Mark the book as available
            books[title].borrower = ''  # Clear the borrower field
        else:
            print(f"Sorry, but {user_name} does not have {title} borrowed.")
    else:
        print(f"{title} not found in the library.")

# Function to handle user login or registration
def user_login(users, user_name):
    user_name = user_name.lower()  # Convert user name to lowercase for consistency
    if user_name not in users:
        print(f"{user_name} does not exist in our database. Creating a new record for you.")
        user_id = f'U_{len(users) + 1:03}'  # Generate a new user ID
        users[user_name] = User(user_name, [user_id, user_name, ''])  # Create a new user record
        print(f"New user created with ID: {user_id}")

# Function to add a new book to the library
def add_new_book(books):
    book_name = input("Enter book name: ").lower()  # Get book name from user and convert to lowercase
    if book_name in books:
        print(f"The book {book_name} is already present in the library.")
    else:
        book_author = input(f"Please enter the author of {book_name}: ").lower()  # Get book author from user
        book_id = f'B_{len(books) + 1:03}'  # Generate a new book ID
        book_details = [book_id, book_name, book_author, 'Yes', '']  # Create book details list
        books[book_name] = Book(book_name, book_details)  # Add new book to the library

# Main function to run the library management system
def main():
    books_path = "books.csv"  # Path to the books CSV file
    users_path = "users.csv"  # Path to the users CSV file
    books = read_csv_file(books_path, Book)  # Read books from the CSV file
    users = read_csv_file(users_path, User)  # Read users from the CSV file

    while True:
        user_name = input("Enter your name: ").lower()  # Get user name and convert to lowercase
        user_login(users, user_name)  # Handle user login or registration
        action = input("Please enter what you want to do (Loan, Return, Add, Exit): ").lower()  # Get user action
        if action == "loan":
            book_name = input(f"Hey {user_name}, please enter the title of the book: ").lower()  # Get book title
            loan_out_book(books, users, book_name, user_name)  # Loan out the book
        elif action == "return":
            book_name = input(f"Hey {user_name}, please enter the title of the book: ").lower()  # Get book title
            return_book(books, users, book_name, user_name)  # Return the book
        elif action == "add":
            add_new_book(books)  # Add a new book to the library
        elif action == "exit":
            book_columns = ['Book ID', 'Title', 'Author', 'Available?', 'Borrower']  # Column names for books CSV
            user_columns = ['User ID', 'Name', 'Borrowed Books']  # Column names for users CSV
            write_csv_file(books_path, book_columns, books)  # Write books to the CSV file
            write_csv_file(users_path, user_columns, users)  # Write users to the CSV file
            break  # Exit the loop
        else:
            print("Invalid option. Please try again.")  # Handle invalid user input

if __name__ == "__main__":
    main()  # Run the main function
