def register_student(student: dict[str, dict[str, str]]) -> None:
    """
    Registers a new student by collecting their name, email, and password, 
    and stores the information in the students_data dictionary.

    Args:
        students_data (dict): A dictionary where student emails are keys 
                               and their details (name and password) are stored as values.
    """
    student_name = input("Ismingizni kiriting :")

    student ['course'] = []
    student_email = input("email manzilini kiriitng :")
    student_password = input("Passwordni kiriting :")

    student['st_login'] = {}
    student['st_login']['login'] = student_email
    student['st_login']['password'] = student_password

    return student
 
def login_student(students_data: dict[str, dict[str, str]]) -> str | None:
    """
    Allows a student to log in by entering their email and password. 
    If the login is successful, it returns the student's name.

    Args:
        students_data (dict): A dictionary where student emails are keys 
                               and their details (name and password) are stored as values.

    Returns:
        str: The student's name if login is successful, else None.
    """
    login = input("email manzilingizni kiriting :")
    password = input("Passwordni kiriting :")

    student_login = {}
    student_login['login'] = login
    student_login['password'] = password

    for user in students_data:
        if(user['st_login']) == student_login:
            print("Siz o'z hisobingizga kirdingiz ")
            return user
        return None
    
def enroll_in_course(
    courses_data: list[dict[str, str]], 
    students_data: dict[str, dict[str, list[str]]], 
    student_email: str
) -> None:
    """
    Allows a student to enroll in a course by selecting from the available courses. 
    The selected course is added to the student's list of enrolled courses.

    Args:
        courses_data (list): A list of dictionaries containing available course details.
        students_data (dict): A dictionary where student emails are keys 
                               and their details (including enrolled courses) are stored as values.
        student_email (str): The email of the student who is enrolling.
    """
    courses_num = int(input("Qaysi kurga qo'shilmoqchisiz :"))

    if courses_num -1 > len(courses_data) or courses_num -1 < 0:
        print("Siz tanlagan kurs mavjud emas ")
        return None
    else :
        print("Siz kurs uchun mafaqiyatli ro'yxatdan o'ttingiz!\n ",format(courses_data[courses_num - 1 ]["course_name"]))