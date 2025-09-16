import sqlite3
from datetime import datetime
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



# Global Database Name
Database_Name = "student_Management.db"

# Create database and table
def create_database():
    """Creates a SQLite database and students table if it doesn't exist."""
    try:
        conn = sqlite3.connect(Database_Name)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                mathematics REAL NOT NULL,
                science REAL NOT NULL,
                english REAL NOT NULL,
                phone TEXT ,
                gmail TEXT,
                average REAL NOT NULL,
                created_date DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()
        conn.close()
        print(f"Database '{Database_Name}' created successfully with 'students' table.")
    except sqlite3.Error as e:
        print(f"Database error: {e}")

# Function to get DB connection
def get_database_connection():
    try:
        return sqlite3.connect(Database_Name)
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None


SUBJECTS = ["Mathematics", "Science", "English"]

# Validate ID and marks
def validate_id_and_marks(student_id, scores):
    conn = get_database_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM students WHERE id=?", (student_id,))
    if cursor.fetchone() is not None:
        conn.close()
        return False, f"Student ID {student_id} already exists in database."

    for score in scores.values():
        if score < 0 or score > 100:
            return False, "Marks must be between 0 and 100."
    conn.close()
    return True, ""

# Validate marks only
def validate_marks(scores):
    for score in scores.values():
        if score < 0 or score > 100:
            return False, "Marks must be between 0 and 100."
    return True, ""

def validate_phone_and_gmail(phone="NA", gmail="NA"):
    phone_pattern = r'^(\+91[-\s]?)?\d{10}$'  # Indian phone pattern example
    gmail_pattern = r'^[a-zA-Z0-9_.+-]+@gmail\.com$'  # Strict Gmail pattern

    if phone != "NA":
        if not re.match(phone_pattern, phone):
            return False, "Invalid phone number format."

    if gmail != "NA":
        if not re.match(gmail_pattern, gmail):
            return False, "Invalid Gmail ID format."

    if phone == "NA" and gmail == "NA":
       pass
    return True, ""


# Insert details into DB
def insert_details():
    student_id = input("Enter student ID: ").strip()
    name = input("Enter student name: ").strip()

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

    is_valid, message = validate_id_and_marks(student_id, scores)
    if not is_valid:
        print(f"Error: {message}")
        return

    phone=input("Enter the Phone Number :").strip()
    gmail=input("enter the Gmail ID:").strip()
    
    is_valid, message = validate_phone_and_gmail(phone, gmail)
    if not is_valid: 
        print(f"Error: {message}")
        return

    average_score = round(sum(scores.values()) / len(scores), 2)

    conn = get_database_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO students (id, name, mathematics, science, english, phone, gmail, average)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (student_id, name, scores["Mathematics"], scores["Science"], scores["English"], phone, gmail, average_score))
    conn.commit()
    conn.close()

    print(f"Student {name} with ID {student_id} added successfully to database.")

# View all records from DB
def view_records():
    conn = get_database_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, mathematics, science, english, phone, gmail, average FROM students")
    records = cursor.fetchall()
    if not records:
        print("No records found.")
    else:
        print("Student Records:\n")
        for row in records:
            print(f"Name: {row[1]}, ID: {row[0]}, Mathematics: {row[2]}, Science: {row[3]}, English: {row[4]} Phone: {row[5]}, Gmail: {row[6]}, Average: {row[7]}")
    conn.close()

# Update student record in DB
def update_records():
    update_id = input("Enter Student ID to update: ").strip()
    conn = get_database_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE id=?", (update_id,))
    record = cursor.fetchone()
    if not record:
        print("No such student found.")
        conn.close()
        return

    print(f"Current Record →Name: {record[1]}, ID: {record[0]}, Mathematics: {record[2]}, Science: {record[3]}, English: {record[4]} Phone: {record[5]}, Gmail: {record[6]}, Average: {record[7]}")

    update_choice = input("What do you want to update? (name/scores/phone/gmail): ").lower()

    if update_choice == "name":
        new_name = input("Enter new name: ")
        cursor.execute("UPDATE students SET name=? WHERE id=?", (new_name, update_id))
        print("Name updated successfully.")

    elif update_choice == "scores":
        scores = {}
        for subject in SUBJECTS:
            scores[subject] = float(input(f"Enter new score for {subject}: "))
        is_valid, message = validate_marks(scores)
        if not is_valid:
            print(f"Error: {message}")
            conn.close()
            return
        avg = round(sum(scores.values()) / 3, 2)
        cursor.execute("""
            UPDATE students SET mathematics=?, science=?, english=?, average=?
            WHERE id=?
        """, (scores["Mathematics"], scores["Science"], scores["English"], avg, update_id))
        print("Scores updated successfully.")
    
    elif update_choice == "phone":
        new_phone = input("Enter new phone number: ").strip()
        is_valid, message = validate_phone_and_gmail(phone=new_phone)
        if not is_valid:
            print(f"Error: {message}")
            conn.close()
            return
        cursor.execute("UPDATE students SET phone=? WHERE id=?", (new_phone, update_id))
        print("Phone number updated successfully.")
    
    elif update_choice == "gmail":
        new_gmail = input("Enter new Gmail ID: ").strip()
        is_valid, message = validate_phone_and_gmail(gmail=new_gmail)
        if not is_valid:
            print(f"Error: {message}")
            conn.close()
            return
        cursor.execute("UPDATE students SET gmail=? WHERE id=?", (new_gmail, update_id))
        print("Gmail ID updated successfully.")

    else:
        print("Invalid choice.")

    conn.commit()
    conn.close()

# Delete student by ID
def delete_record():
    delete_id = input("Enter Student ID to delete: ").strip()
    conn = get_database_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id=?", (delete_id,))
    conn.commit()
    if cursor.rowcount > 0:
        print(f"Student {delete_id} deleted successfully.")
    else:
        print("No such student found.")
    conn.close()

# Analyze student data
def analyze():
    analyze_menu = """\nSelect Option:
[0] Menu
[1] Show Topper
[2] Failed Students
[3] Class Average
[4] All Students with Average
[5] Exit
"""
    print(analyze_menu)
    conn = get_database_connection()
    cursor = conn.cursor()

    while True:
        choice = int(input("Enter choice (0-5): "))

        if choice == 0:
            print(analyze_menu)
        elif choice == 1:  # topper
            cursor.execute("SELECT * FROM students ORDER BY average DESC LIMIT 1")
            topper = cursor.fetchone()
            if topper:
                print(f"Topper: {topper[1]} ({topper[0]}) → Avg: {topper[5]}")
        elif choice == 2:  # failed students
            cursor.execute("SELECT * FROM students WHERE average <= 35")
            fails = cursor.fetchall()
            for f in fails:
                print(f"Failed: {f[1]} ({f[0]}) → Avg: {f[5]}")
        elif choice == 3:  # class average
            cursor.execute("SELECT AVG(average) FROM students")
            avg = cursor.fetchone()[0]
            print(f"Class Average: {round(avg, 2) if avg else 'N/A'}")
        elif choice == 4:  # all
            cursor.execute("SELECT * FROM students")
            all_students = cursor.fetchall()
            for s in all_students:
                print(f"{s[1]} ({s[0]}) → Avg: {s[5]}")
        elif choice == 5:
            break
        else:
            print("Invalid choice.")

    conn.close()

# Initialize DB
create_database()

# Menu-driven logic
menu = """
[0] Show Menu
[1] Insert Student
[2] View Students
[3] Update Student
[4] Analyze Students
[5] Delete Student
[6] Exit
"""
print(menu)

while True:
    try:
        choice = int(input("Choose (0-6): "))
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
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")
    except ValueError:
        print("Please enter a number.")
