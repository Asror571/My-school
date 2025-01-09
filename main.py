from school import students, courses, grades

def main():
    """
    Main function that drives the On-School system. It displays the main menu, 
    handles user registration and login, and provides an interface for enrolled students 
    to interact with courses and check grades.
    """
    student = {}
    students_data = []
    courses_data = [
        {"course_name": "Python Basics", "instructor": "John Doe", "duration": "8 weeks", "price": 500},
        {"course_name": "Data Science 101", "instructor": "Jane Smith", "duration": "10 weeks", "price": 780}
    ]
    grades_data = {}

    while True:
        print("My School maktabiga , Xush kelibsiz!")
        print("1.Ro'yxatdan o'tish","2.Login","3.Chiqish",sep='\n')
        user_chose = int(input("Qaysi bo'limga kirasiz :"))

        if user_chose == 1:
            yanigi_student = students.register_student(student)
            
            students_data.append(yanigi_student)
        
        elif user_chose == 2:
            user = students.login_student(students_data)

            while user:
                print("\n--- Main Menu for Alice Smith --- \n1. View Available Courses\n2. Enroll in a Course\n3. View My Courses\n4. Check My Grades\n5. Logout\n6. exit")

                comand_user = int(input("Bo'limlardan birini tanlang :"))
                if comand_user == 1:
                    courses.view_courses(courses_data)
                
                elif comand_user == 2:
                    student['course'].append(students.enroll_in_course(courses_data, students_data, student['st_login']['login']))
                
                elif comand_user == 3:
                    print(student)
                    courses.view_courses(student['course'])
                
                elif comand_user == 4:
                    grades.check_grades(user, grades_data)
                
                elif comand_user == 5:
                    break
                
                elif comand_user == 6:
                    exit()
                else:
                    print("\nSiz mavjud bo'lmagan buyuruqni tanladingiz \n")


if __name__ == "__main__":
    main()
