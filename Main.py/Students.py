class Student:
        all_students = []
        def __init__(self, name, roll_number, marks):
            self.name = name
            self.roll_number = roll_number
            self.marks = marks

@classmethod
def add_student(cls):
        name = input("Enter student name: ")
        roll_number = input("Enter roll number: ")
        marks = float(input("Enter marks: "))
        student = cls(name, roll_number, marks)
        cls.all_students.append(student)
        print("Student added successfully!")

@classmethod
def update_marks(cls):
        roll_number = input("Enter roll number of the student to update marks: ")
        for student in cls.all_students:
            if student.roll_number == roll_number:
                new_marks = float(input("Enter new marks: "))
                student.marks = new_marks
                print("Marks updated successfully!")
                return
        print("Student not found!")

@classmethod
def show_all_students(cls):
        if not cls.all_students:
            print("No students found.")
        else:
            print("\nList of all students:")
            for student in cls.all_students:
                print(f"Name: {student.name}, Roll Number: {student.roll_number}, Marks: {student.marks}")

@staticmethod
def menu():
    while True:
        print("\n ============= Student management system =============")
        print("1. Add Student")
        print("2. Update Marks")
        print("3. Show All Students")
        print("4. Exit")

        choice = input("Enter your choice(1-4): ")
        if choice == "1":
           Student.add_student()
        elif choice == "2":
             Student.update_marks()
        elif choice == "3":
             Student.show_all_students()
        elif choice == "4":
             print("Exiting Student management system. Goodbye!")
        break
    else:
         print("Invalid choice. Please try again.")


if __name__ == "__main__":
    Student.menu()
                
