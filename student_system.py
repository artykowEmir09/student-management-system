
students = []

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add student")
    print("2. Show students")
    print("3. Search student")
    print("4. Remove student")
    print("5. Update student")
    print("6. Count students")
    print("7. Sort students")
    print("8. Clear all students")
    print("9. Exit")
    print("=====================================")

    choice = input("Choose an option: ")

    # ADD STUDENT
    if choice == "1":
        print("\n====== ADD STUDENT ======")

        student = input("Enter student name: ").strip()

        if not student:
            print("Name cannot be empty!")

        elif student.lower() in [x.lower() for x in students]:
            print("Student already exists!")

        else:
            students.append(student)
            print("Student added successfully!")

    # SHOW STUDENTS
    elif choice == "2":
        print("\n====== SHOW STUDENTS ======")

        if len(students) == 0:
            print("No students available.")

        else:
            for index, student in enumerate(students, start=1):
                print(index, ".", student)

    # SEARCH STUDENT
    elif choice == "3":
        print("\n====== SEARCH STUDENT ======")

        name = input("Enter student name: ").strip()

        found = False

        for student in students:
            if student.lower() == name.lower():
                print(student, "found!")
                found = True
                break

        if not found:
            print("Student not found!")

    # REMOVE STUDENT
    elif choice == "4":
        print("\n====== REMOVE STUDENT ======")

        delete = input("Enter student name: ").strip()

        for student in students:
            if student.lower() == delete.lower():
                students.remove(student)
                print("Student removed successfully!")
                break
        else:
            print("Student not found!")

    # UPDATE STUDENT
    elif choice == "5":
        print("\n====== UPDATE STUDENT ======")

        old_name = input("Enter current name: ").strip()

        for index, student in enumerate(students):
            if student.lower() == old_name.lower():

                new_name = input("Enter new name: ").strip()

                if not new_name:
                    print("Name cannot be empty!")

                elif new_name.lower() in [x.lower() for x in students]:
                    print("This student name already exists!")

                else:
                    students[index] = new_name
                    print("Student updated successfully!")

                break
        else:
            print("Student not found!")

    # COUNT STUDENTS
    elif choice == "6":
        print("\n====== STUDENT COUNT ======")
        print("Total students:", len(students))

    # SORT STUDENTS
    elif choice == "7":
        print("\n====== SORT STUDENTS ======")

        students.sort(key=str.lower)

        print("Students sorted alphabetically!")

        for student in students:
            print(student)

    # CLEAR ALL STUDENTS
    elif choice == "8":
        print("\n====== CLEAR STUDENTS ======")

        confirm = input("Are you sure? (yes/no): ")

        if confirm.lower() == "yes":
            students.clear()
            print("All students removed!")

        else:
            print("Operation cancelled.")

    # EXIT
    elif choice == "9":
        print("Thank you for using Student Management System!")
        break

    else:
        print("Invalid choice! Please try again.")
