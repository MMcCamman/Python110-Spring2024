# ------------------------------------------------------------------------------------------ #
# Title: Working with file data
# Desc: Shows how save data to a file
# Change Log: (Who, When, What)
#   McCamman, 2024-05-03,Created Script
#   McCamman, 2024-05-10, Modified to json
#   McCamman, 2024-05-10, Included Try-Except
# ------------------------------------------------------------------------------------------ #

# Libraries
import json

# Define the program's data
MENU: str = '''
---- Student GPAs ------------------------------
  Select from the following menu:  
    1. Show current student data. 
    2. Enter new student data.
    3. Save data to a file.
    4. Exit the program.
-------------------------------------------------- 
'''
FILE_NAME: str = 'MyLabData.json'
student_first_name: str = ''
student_last_name: str = ''
student_gpa: float = 0.0
message: str = ''
menu_choice: str = ''
student_data: dict = {}  # one row of student data
students: list = []  # a table of student data
file_data: str = ''
file = None  # Not using type hint helps PyCharm, so we won't use it going forward

# When the program starts, read the file data into a list of lists (table)

try:
    file = open(FILE_NAME, "r")
    students = json.load(file)
    file.close()
except FileNotFoundError as e:
    print("Text file must exist before running this script!\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')
except Exception as e:
    print("There was a non-specific error!\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')
finally:
    if file.closed == False:
        file.close()



# Repeat the follow tasks
while True:
    print(MENU)
    menu_choice = input("Enter your menu choice number: ")
    print()  # Adding extra space to make it look nicer.

    # Process the data to create and display a custom messages
    if menu_choice == "1":
        # Process the data to create and display a custom message
        print("-" * 50)
        for student in students:
            if student["GPA"] >= 4.0:
                message = " {} {} earned an A with a {:.2f} GPA"
            elif student["GPA"] >= 3.0:
                message = " {} {} earned a B with a {:.2f} GPA"
            elif student["GPA"] >= 2.0:
                message = " {} {} earned a C with a {:.2f} GPA"
            elif student["GPA"] >= 1.0:
                message = " {} {} earned a D with a {:.2f} GPA"
            else:
                message = " {} {}'s {:.2f} GPA was not a passing grade"

            print(message.format(student["FirstName"], student["LastName"], student["GPA"]))
        print("-" * 50)
    elif menu_choice == "2":
        # Input the data
        try:
            # Input the data
            student_first_name = input("What is the student's first name? ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")

            student_last_name = input("What is the student's last name? ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")

            try:  # using a nested try block to capture when an input cannot be changed to a float
                student_gpa = float(input("What is the student's GPA? "))
            except ValueError:
                raise ValueError("GPA must be a numeric value.")

            student_data = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "GPA": float(student_gpa)}
            students.append(student_data)
        except ValueError as e:
            print(e)  # Prints the custom message
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())
        except Exception as e:
            print("There was a non-specific error!\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')



    # Save the data to the file
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file)
            file.close()
            continue
        except TypeError as e:
            print("Please check that the data is a valid JSON format\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')
        except Exception as e:
            print("-- Technical Error Message -- ")
            print("Built-In Python error info: ")
            print(e, e.__doc__, type(e), sep='\n')
        finally:
            if file.closed == False:
                file.close()
        continue

    # out of the while loop
    elif menu_choice == "4":
        break  # out of the while loop