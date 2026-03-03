# Course Enrollment Management Module
# Pair Programming Practice - XP

# -------------------------------
# ITERATION 1
# Driver: Swaroop
# Navigator: Akash Bhat
# Implemented:
# 1. add_course()
# 2. enroll_student()
# -------------------------------

courses = []
enrollments = {}

def add_course():
    course_name = input("Enter course name to add: ").strip()
    if course_name in courses:
        print("Course already exists.")
    else:
        courses.append(course_name)
        print("Course added successfully.")

def enroll_student():
    student_name = input("Enter student name: ").strip()
    course_name = input("Enter course name to enroll in: ").strip()

    if course_name not in courses:
        print("Course does not exist.")
        return

    if student_name not in enrollments:
        enrollments[student_name] = []

    if course_name in enrollments[student_name]:
        print("Student already enrolled in this course.")
    else:
        enrollments[student_name].append(course_name)
        print("Student enrolled successfully.")


# -------------------------------
# ROLE SWITCHING
# Driver: Akash Bhat
# Navigator: Swaroop
# -------------------------------


# -------------------------------
# ITERATION 2
# Implemented:
# 3. drop_course()
# 4. view_enrolled_courses()
# Code improvements and validation
# -------------------------------

def drop_course():
    student_name = input("Enter student name: ").strip()
    course_name = input("Enter course name to drop: ").strip()

    if student_name not in enrollments:
        print("Student not found.")
        return

    if course_name not in enrollments[student_name]:
        print("Student is not enrolled in this course.")
    else:
        enrollments[student_name].remove(course_name)
        print("Course dropped successfully.")

def view_enrolled_courses():
    student_name = input("Enter student name: ").strip()

    if student_name not in enrollments or len(enrollments[student_name]) == 0:
        print("No courses enrolled.")
    else:
        print("Enrolled courses:")
        for course in enrollments[student_name]:
            print(course)


# -------------------------------
# MENU SYSTEM (Integrated Final Module)
# -------------------------------

def menu():
    while True:
        print("\n--- Course Enrollment System ---")
        print("1. Add Course")
        print("2. Enroll Student")
        print("3. Drop Course")
        print("4. View Enrolled Courses")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_course()
        elif choice == "2":
            enroll_student()
        elif choice == "3":
            drop_course()
        elif choice == "4":
            view_enrolled_courses()
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")

menu()