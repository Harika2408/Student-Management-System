import sqlite3

# Connect to SQLite (creates database if not exists)
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    roll_no INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    course TEXT NOT NULL,
    marks INTEGER
)
""")
conn.commit()


def add_student(roll_no, name, course, marks):
    cursor.execute("INSERT INTO students VALUES (?, ?, ?, ?)", (roll_no, name, course, marks))
    conn.commit()
    print("✅ Student added successfully!")


def view_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    print("\n--- Student Records ---")
    for row in rows:
        print(row)


def search_student(roll_no):
    cursor.execute("SELECT * FROM students WHERE roll_no=?", (roll_no,))
    row = cursor.fetchone()
    if row:
        print("🎓 Student Found:", row)
    else:
        print("⚠️ Student not found!")


def update_student(roll_no, name, course, marks):
    cursor.execute("UPDATE students SET name=?, course=?, marks=? WHERE roll_no=?", (name, course, marks, roll_no))
    conn.commit()
    print("✏️ Student updated successfully!")


def delete_student(roll_no):
    cursor.execute("DELETE FROM students WHERE roll_no=?", (roll_no,))
    conn.commit()
    print("🗑️ Student deleted successfully!")


# Menu
while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        r = int(input("Roll No: "))
        n = input("Name: ")
        c = input("Course: ")
        m = int(input("Marks: "))
        add_student(r, n, c, m)

    elif choice == "2":
        view_students()

    elif choice == "3":
        r = int(input("Enter Roll No to search: "))
        search_student(r)

    elif choice == "4":
        r = int(input("Roll No: "))
        n = input("New Name: ")
        c = input("New Course: ")
        m = int(input("New Marks: "))
        update_student(r, n, c, m)

    elif choice == "5":
        r = int(input("Enter Roll No to delete: "))
        delete_student(r)

    elif choice == "6":
        print("👋 Exiting...")
        break

    else:
        print("❌ Invalid choice, try again.")
