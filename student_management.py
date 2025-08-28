import sqlite3

# Connect to database (creates one if not exists)
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    course TEXT NOT NULL,
    marks INTEGER
)
""")
conn.commit()


# Function to add student
def add_student(name, course, marks):
    cursor.execute("INSERT INTO students (name, course, marks) VALUES (?, ?, ?)", (name, course, marks))
    conn.commit()
    print("✅ Student added successfully!")


# Function to view all students
def view_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    print("\n📋 Student Records:")
    for row in rows:
        print(row)


# Function to update student marks
def update_student(student_id, marks):
    cursor.execute("UPDATE students SET marks = ? WHERE id = ?", (marks, student_id))
    conn.commit()
    print("✏️ Student updated successfully!")


# Function to delete student
def delete_student(student_id):
    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    print("🗑️ Student deleted successfully!")


# Menu-driven program
def main():
    while True:
        print("\n==== Student Management System ====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student Marks")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            course = input("Enter course: ")
            marks = int(input("Enter marks: "))
            add_student(name, course, marks)

        elif choice == "2":
            view_students()

        elif choice == "3":
            student_id = int(input("Enter Student ID to update: "))
            marks = int(input("Enter new marks: "))
            update_student(student_id, marks)

        elif choice == "4":
            student_id = int(input("Enter Student ID to delete: "))
            delete_student(student_id)

        elif choice == "5":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice! Try again.")


if __name__ == "__main__":
    main()
    conn.close()

