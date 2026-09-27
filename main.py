import sqlite3

def init_db():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            course TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_student(name, age, course):
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO students (name, age, course) VALUES (?, ?, ?)', (name, age, course))
    conn.commit()
    conn.close()
    print("Student added successfully!")

def view_students():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM students')
    rows = cursor.fetchall()
    conn.close()
    print("\n--- Student List ---")
    for row in rows:
        print(f"ID: {row[0]} | Name: {row[1]} | Age: {row[2]} | Course: {row[3]}")
    print("---------------------\n")

def main():
    init_db()
    while True:
        print("1. Add Student")
        print("2. View Students")
        print("3. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            course = input("Enter Course: ")
            add_student(name, age, course)
        elif choice == '2':
            view_students()
        elif choice == '3':
            break
        else:
            print("Invalid choice!")

if __name__ == '__main__':
    main()