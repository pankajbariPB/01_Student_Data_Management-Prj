
"""
Project Title: Student Data Management and Analysis Tool
============================================================================= 

Author:
Pankaj bari

Version:
 5.6
Description:
This project is designed as part of my Python learning journey.
  Its goal is to collect, manage, and analyze data from students. 
  The project will allow me to practice key concepts such as data collection, 
  processing, and analysis. 
  It will also include features to generate personalized results and insights,
  for the students based on their data.

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
students=[]
SUBJECTS=["Mathematics","Science","English"]
 
# ID MARKS VALID
def validate_id_and_marks(student_id:str,scores:list[float]):    
    """
    validates student ID and Marks.

    Args:
    student_id (str): The ID of the student to validate.
    scores (list[float]): List of scores to validate.

    returns:
        bool value
        error message
    """
    for student in students:
        if student["id"] == student_id: 
            return False,f"Please enter unique student id instead {student['id']}"
        
    for score in scores:
         if any(score < 0 or score > 100 for score in scores.values()):
            return False,f"Invalid marks , marks must be between 0 and 100...!"
    return True,""

#valid marks while updating 
def validate_marks(scores:list[float]):
    for score in scores:
         if any(score < 0 or score > 100 for score in scores.values()):
            return False,f"Invalid marks , marks must be between 0 and 100...!"
    return True,""

 #INSERT FUNCTION           
def insert_details():    
    """
    Collects student details and inserts them into the students list.
    """
    student_id = input("Enter student ID: ").strip()
    name = input("Enter student name: ").strip()
    
    #collecting scores
    scores = {}
    for subject in SUBJECTS:
        while True:
            try:
                score = float(input(f"Enter score for {subject} (0-100): "))
                if 0 <= score <= 100:
                    scores[subject] = score
                    break
                else:
                    print("Score must be between 0 and 100. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

    #validate id and marks
    is_valid,message=validate_id_and_marks(student_id,scores)
    if not is_valid:
        print(f"Error: {message}")
        return

    #calculate average
    average_score = round(sum(scores.values()) / len(scores), 2)

    #create student record
    student_record = {
        "id": student_id,
        "name": name,
        "scores": scores,
        "average": average_score
    }
    
    #insert record into list
    students.append(student_record)
    
    print(f"Student {name} with ID {student_id} added successfully.")
#VIEW RECORDS FUNCTION
def view_records():
    """
    Displays all student details in a formatted manner.
    """
    print("Student Records:")
    for student in students:
        math,sci,eng=student['scores'].values() #unpacking the subj from scores{} to variable 
        print(f"Name: {student['name']} , ID: {student['id']} , mathematics: {math} , science: {sci} , english :{eng}")

#UPDATE FUNTION
def update_records():
    """
    Update the student records into list 
    """
    update_id=input("Provide ID to update records :").strip()
    for student in students:
        if update_id==student['id']:
            math,sci,eng=student['scores'].values()
            print(f"Record to be updated is : Name :{student['name']} , ID : {student['id']} , mathematics: {math} , science: {sci} , english :{eng} \n")
            valid=input('"yes/no" is this your record...? :').lower()
            if valid=='yes':
                update_data=input("\n what you want to change...? 'name/id/scores' :").lower()
                if update_data=='name': 
                    print(f"previous {update_data} is {student[update_data]}")
                    updated_data=input(f"Enter new {update_data} to insert in records :")
                    student[update_data]=updated_data
                    print(f"{update_data} {updated_data} updated succesfully")
                    return
                if update_data=='scores':
                    print(f"previous {update_data} is {student[update_data]}")
                    updated_scores={}
                    for subject in SUBJECTS:
                        new_score=float(input(f"Enter the score in {subject} \t\t:"))
                        updated_scores[subject]=new_score
                    is_update_valid,message = validate_marks(updated_scores)
                    #validate update before insert
                    if not is_update_valid:
                        print(f"Error: {message}")
                        return
                    # insert updates scores    
                    student[update_data]=updated_scores
                    print(f"{update_data} {updated_scores} inserted succesfully")
                    return
                if update_data=='id':
                    print(f"previous {update_data} is {student[update_data]}")
                    print("can't update id, you must delete that record first :")
                    delete_record(student['id'])
                    return

analyze_menu="""\nwhat you want to analyze ?
[0] to see menu.
[1] to see topper.
[2] failed students.
[3] average score of class.
[4] see average of all class.
[5] to exit menu.\n"""
def analyze():
    print(analyze_menu)
    for student in students:
        marks = student["scores"].values()
        avg=round(sum(marks)/len(marks),2)
        student["average"]=avg
    while True:
        analyze_choice=int(input("select analysis type (0-4):"))
        
        if analyze_choice == 0:
            print(analyze_menu)
        if analyze_choice == 1:
            
            
            highest_scorer = max(students , key=lambda x:x["average"])
            math,sci,eng=highest_scorer['scores'].values() #unpacking the subj from scores{} to variable 
            print(f"\nName: {highest_scorer['name']} , ID: {highest_scorer['id']} , mathematics: {math} , science: {sci} , english :{eng} with percentage {highest_scorer['average']} \n")    
                                    
        if analyze_choice == 2:
                    
                    print("\n")
                    for student in students:
                        if student['average'] <= 35:  
                            print(f"Name: {student['name']} , ID: {student['id']} , mathematics: {math} , science: {sci} , english :{eng} FAILED with percentage {student['average']} ")    
        
        if analyze_choice == 3:
           total_students = len(students)
           if total_students == 0:
               print("No students to analyze.")
               continue
           total_score = sum(student["average"] for student in students)
           average_score = round(total_score / total_students, 2)
           print(f"\nAverage score of the class is {average_score}\n")
                       
        if analyze_choice == 4:
            for student in students:
                print(f"\nName: {student['name']} , ID: {student['id']} , mathematics: {math} , science: {sci} , english :{eng} with percentage {student['average']} \n")    
               
        if analyze_choice == 5:
            print("Exiting analysis menu...")
            break
def delete_record(student_id=None):
    """
    Deletes a student record based on the provided ID.
    """
    delete_id = input("Enter the ID of the student to delete: ").strip()
    for student in students:
        if student['id'] == delete_id:
            students.remove(student)
            print(f"Record with ID {delete_id} deleted successfully.")
            return
    print(f"No record found with ID {delete_id}.")

# menu option
menu="""[0] to view menu.
[1] to insert student details.
[2] to view all records.
[3] to update details.
[4] to analyze all details.
[5] to delete a student record.
[6] to exit Menu """
print(menu)

# menu driven logic
while True:
    # try block containing risky code
    try:
        choice=int(input("\nSelect the option to start (0-6) :"))
        if choice == 0:
            print(menu)
        elif choice == 1:
            insert_details()
        elif choice == 2:
          view_records()
        elif choice == 3:
            update_records()
        elif choice == 4:
            analyze()
        elif choice == 5:
            delete_record()
        elif choice == 6:
            print("Visit again..! Thank you for using system")
            break
        else:
            print("Invalid choice")
    except ValueError :
        print("Enter valid choice between 1 to 6.")
    
 