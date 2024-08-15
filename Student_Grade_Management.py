import csv

class Student:
    """
    A class to represent a student.

    Attributes:
    ----------
    name : str
        The name of the student.
    grades : list
        A list of grades for the student.

    Methods:
    -------
    display():
        Prints the student's name and grades.
    data():
        Returns the student's name and grades.
    std_grade():
        Returns the student's grades.
    avg_grade():
        Calculates and returns the average grade of the student.
    pass_fail():
        Determines if the student has passed or failed based on the average grade.
    """

    def __init__(self, name, grades) -> None:
        """
        Constructs all the necessary attributes for the student object.

        Parameters:
        ----------
        name : str
            The name of the student.
        grades : list
            A list of grades for the student.
        """
        self.name = name
        self.grades = [float(grade) for grade in grades]

    def display(self):
        """Prints the student's name and grades."""
        print(f"{self.name} has grades: {self.grades}")

    def data(self):
        """Returns the student's name and grades."""
        return self.name, self.grades

    def std_grade(self):
        """Returns the student's grades."""
        return self.grades

    def avg_grade(self):
        """Calculates and returns the average grade of the student."""
        if not self.grades:
            return 0
        return round(sum(self.grades) / len(self.grades), 2)

    def pass_fail(self):
        """Determines if the student has passed or failed based on the average grade."""
        return result(self.avg_grade())

def read_file(file_path):
    """
    Reads student data from a CSV file and returns a dictionary of student objects.

    Parameters:
    ----------
    file_path : str
        The path to the CSV file.

    Returns:
    -------
    dict
        A dictionary to store student objects.
    """
    classname = {}
    try:
        with open(file_path, "r") as student_file:
            reader = csv.reader(student_file)
            next(reader)  # Skip header
            for row in reader:
                name = row[0].lower()
                grades = row[1:4]
                classname[name] = Student(name, grades)
    except FileNotFoundError:
        print("No record found.")
    return classname

def write_file(file_path, classname):
    """
    Writes student data to a CSV file.

    Parameters:
    ----------
    file_path : str
        The path to the CSV file.
    classname : dict
        A dictionary to store student objects.
    """
    with open(file_path, "w", newline='') as student_file:
        writer = csv.writer(student_file)
        writer.writerow(['Name', 'Maths', 'English', 'Science', 'Avg'])
        for name, student in classname.items():
            grades = student.std_grade()
            avg = student.avg_grade()
            writer.writerow([name] + grades + [avg])

def add_student(name, grades, classname):
    """
    Adds a new student to the classname dictionary.

    Parameters:
    ----------
    name : str
        The name of the student.
    grades : list
        A list of grades for the student.
    classname : dict
        A dictionary to store student objects.
    """
    if name.lower() in classname:
        print(f"{name} is already present in our database, please add a different student.")
    else:
        classname[name.lower()] = Student(name.lower(), grades)

def remove_student(name, classname):
    """
    Removes a student from the classname dictionary.

    Parameters:
    ----------
    name : str
        The name of the student to be removed.
    classname : dict
        A dictionary to store student objects.
    """
    if name.lower() in classname:
        del classname[name.lower()]
    else:
        print(f"{name} is not in our database.")

def result(num):
    """
    Determines if a student has passed based on their average grade.

    Parameters:
    ----------
    num : float
        The average grade of the student.

    Returns:
    -------
    bool
        True if the student has passed, False otherwise.
    """
    return num > 33

def generate_report_card(student, file_path):
    """
    Generates a report card for a specific student and saves it to a text file.

    Parameters:
    ----------
    student : Student
        The student object for which the report card is generated.
    file_path : str
        The path where the report card file will be saved.
    """
    with open(file_path, "w") as report_file:
        report_file.write(f"Report Card for {student.name.capitalize()}\n")
        report_file.write("="*30 + "\n")
        grades = student.std_grade()
        report_file.write(f"Maths: {grades[0]}\n")
        report_file.write(f"English: {grades[1]}\n")
        report_file.write(f"Science: {grades[2]}\n")
        avg = student.avg_grade()
        report_file.write(f"Average: {avg}\n")
        result_status = "Passed" if student.pass_fail() else "Failed"
        report_file.write(f"Result: {result_status}\n")

def main():
    """
    The main function to interact with the user and perform various operations
    such as reading, adding, removing students, calculating averages, determining results,
    and generating report cards.
    """
    file_path = "C:\\Users\\dingodara\\Desktop\\pf\\Python\\Student.csv"
    classname = read_file(file_path)

    while True:
        user_in = input("Please enter what you want to do, options: Read, Add, Remove, Avg, Result, Report, Exit: ").lower()
        if user_in == "read":
            user_in2 = input("Do you want to show all results or a specific result: ").lower()
            if user_in2 == "all":
                for name, student in classname.items():
                    grades = student.std_grade()
                    print(f'{name} scored {grades[0]} in Maths, {grades[1]} in English, and {grades[2]} in Science.')
            elif user_in2 == "specific":
                name = input("Enter the name for which you want to see the score: ").lower()
                student = classname.get(name)
                if student:
                    grades = student.std_grade()
                    print(f'{name} scored {grades[0]} in Maths, {grades[1]} in English, and {grades[2]} in Science.')
                else:
                    print(f"We are not able to find any record related to {name}.")

        elif user_in == "add":
            try:
                user_in2 = input("Please enter the name: ")
                maths = float(input("Please enter marks scored in Maths: "))
                english = float(input("Please enter marks scored in English: "))
                science = float(input("Please enter marks scored in Science: "))
                grades = [maths, english, science]
                add_student(user_in2, grades, classname)
                print(f'{user_in2} scored {grades[0]} in Maths, {grades[1]} in English, and {grades[2]} in Science.')
            except ValueError:
                print("Invalid data entered, please recheck.")

        elif user_in == "avg":
            user_in2 = input("Do you want to show all student averages or a specific student: ").lower()
            if user_in2 == "all":
                for name, student in classname.items():
                    avg = student.avg_grade()
                    print(f'{name} has an average score of {avg}.')
            elif user_in2 == "specific":
                name = input("Enter the name for which you want to see the score: ").lower()
                student = classname.get(name)
                if student:
                    avg = student.avg_grade()
                    print(f'{name} has an average score of {avg}.')
                else:
                    print(f"We are not able to find any record related to {name}.")

        elif user_in == "remove":
            user_in2 = input("Please enter the name: ").lower()
            remove_student(user_in2, classname)

        elif user_in == "result":
            user_in2 = input("Do you want to show all student results or a specific student: ").lower()
            if user_in2 == "all":
                for name, student in classname.items():
                    result_status = "passed" if student.pass_fail() else "failed"
                    print(f'{name} has {result_status}.')
            elif user_in2 == "specific":
                name = input("Enter the name for which you want to see the score: ").lower()
                student = classname.get(name)
                if student:
                    result_status = "passed" if student.pass_fail() else "failed"
                    print(f'{name} has {result_status}.')
                else:
                    print(f"We are not able to find any record related to {name}.")

        elif user_in == "report":
            name = input("Enter the name for which you want to generate the report card: ").lower()
            student = classname.get(name)
            if student:
                report_file_path = f"C:\\Users\\dingodara\\Desktop\\pf\\Python\\{name}_report_card.txt"
                generate_report_card(student, report_file_path)
                print(f"Report card generated for {name} at {report_file_path}.")
            else:
                print(f"We are not able to find any record related to {name}.")

        elif user_in == "exit":
            write_file(file_path, classname)
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
