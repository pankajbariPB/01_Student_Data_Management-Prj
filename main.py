"""
Author: Pankaj Bari
Version: 5.1

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
    a. Display a menu for user options: Add student, View student,
       Update student, Delete student, View analytics, Exit.

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


#global variables
id_valid=True
marks_valid=True
check =True
students=[]

# this function will check for legal data insertion i.e.. id and marks. 
def validate_id_marks(subs_score):        
    for s in students:
        if s['id'] in id:    
            print("Please enter unique student id instead ",s["id"])
            id_valid=False
            print("Warning!!! this data will not be added to records")
    for i in subs_score:
        if not( 0 <= i <=100 ):
            print("Invalid marks, marks must be between 0 and 100...!\nWarning!!! this data will not considered")
            marks_valid=False
   
  
# function to input details from end user
def insert_details():    
    name = input("\nEnter the name of the student\t:")
    id=input("Enter the ID of student\t\t:")  
    math=float(input("Enter the marks in mathematics\t:"))            
    sci=float(input("Enter the marks in science\t:")) 
    eng=float(input("Enter the marks in english\t:"))
    subs_score=[math,sci,eng]
    
    # calling function
    validate_id_marks()
    
    #inserting valid data
    if(id_valid and marks_valid == True):
        student_data={"name":name,"id":id,"score":subs_score}
        students.append(student_data)

# menu option
print("1. Press 1 to  insert details.")
print("2. Press 2 to view all details")
print("3. Press 3 to update details")
print("4. Press 4 to analyze all details")
print("5. Press 5 to delete a student")
print("6. Press 6 to exit Menu ")

# menu driven logic
while check:
    # Error handing block containg risky code
    try:
        choice=int(input("\n--Select-choice-from--> 1:Insert, 2:View, 3:Update, 4:Analyse, 5:Delete, 6:Exit -->\t",))
        if choice == 1:
            insert_details()
       
        elif choice == 2:
            for i in students:
                print(i)
                
        elif choice == 6:
            print("Visit again...!")
            check = False
    
        else:
            print("Invalid choice")
    except ValueError as ve:
        print("Enter valid choice between 1 to 6.",ve)
    
 