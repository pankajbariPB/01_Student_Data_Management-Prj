"""
Project Title: Student Data Management and Analysis
 
Description:
This project is designed as part of my Python learning journey. Its goal is to collect, manage, and analyze data from students. 
The project will allow me to practice key concepts such as data collection, processing, and analysis. 
It will also include features to generate personalized results and insights for the students based on their data.

< core Python topics to your Python project.>
Variables, data types, and operators
Input/output
Conditional statements and loops
Functions
Lists, dictionaries, and tuples
File handling
Exception handling
Object-oriented programming (classes and objects)
Modules and packages
Regular expressions
JSON handling (JSON, XML, CSV optional)
Basic data visualization (optional)

Features :
1. Main Menu
    a. Display a menu for user options: Add student, View student, Update student, Delete student, View analytics, Exit.

2. Add Student
    a. Input: Name, age, grade, and scores (in multiple subjects).
    b. Store the student information in a dictionary or JSON file.

3. View Students
a. Display all students' data in a formatted way.
b. Implement search functionality using student names or IDs.

4. Update Student
    a. Allow users to update any field of an existing student's record.

5. Delete Student.
a. Allow deletion of a student record by ID.

6. Analytics Reports
    a. Calculate the class average score.
    b. Display the top-performing student.
    c. Visualize student scores using basic graphs (optional).

7. Error Handling
    a. Handle invalid inputs gracefully.
    b. Handle cases where files are missing or empty.

8. File Handling
    a. Save all student records to a JSON file.
    b. Load data from the file when the program starts.

9. Object-Oriented Design
    a. Use classes such as Student, StudentManager, and Analytics.

10. Regular Expressions
    a. Validate input like email or phone number if added.
"""
print("1. Press 1 to  insert details.")
print("2. Press 2 to view all details")
print("3. Press 3 to update details")
print("4. Press 4 to analyze all details")
print("5. Press 5 to delete a student")
print("6. Press 6 to exit Menu")
check =True
while check:
    choice=int(input("Enter a choice..."))
    if choice==1:
        name = input("Enter the name of the student: ")
        roll_no=input("Enter the roll number: ")                 # bug not same
        math=float(input("Enter the marks in mathematics:"))            # what if absent? , enter 0
        sci=float(input("Enter the marks in science:")) 
        eng=float(input("Enter the marks in english:"))
        print("marks collected")
    elif choice==5:
        check = False
