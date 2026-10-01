class Student:
    def __init__(self,id,name,dob):
        self.__id = id
        self.__name = name
        self.__dob = dob
        self.__marks = {}     
 
    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name
 
    def set_mark(self, course_id, mark):
        self.__marks[course_id] = mark
 
    def get_mark(self, course_id):
        return self.__marks.get(course_id, "N/A")
 
    def input(self):
        self.__id = input("  ID: ")
        self.__name = input("  Name: ")
        self.__dob = input("  Date of birth: ")
 
    def list(self):
        print(f"{self.__id:<8}{self.__name:<20}{self.__dob}")
 
 
class Course:
    def __init__(self,id,name):
        self.__id =id
        self.__name =name
 
    def get_id(self):
        return self.__id
 
    def get_name(self):
        return self.__name
 
    def input(self):
        self.__id = input("  ID: ")
        self.__name = input("  Name: ")
 
    def list(self):
        print(f"{self.__id:<8}{self.__name}")
 
 
students = []
courses = []
 
 
def input_students():
    n = int(input("Number of students: "))
    for i in range(n):
        print(f"Student {i + 1}:")
        s = Student()
        s.input()
        students.append(s)
 
 
def input_courses():
    n = int(input("Number of courses: "))
    for i in range(n):
        print(f"Course {i + 1}:")
        c = Course()
        c.input()
        courses.append(c)
 
 
def find_course(cid):
    for c in courses:
        if c.get_id() == cid:
            return c
    return None
 
 
def input_marks():
    list_courses()
    c = find_course(input("Select course ID: "))
    if c is None:
        print("Course not found.")
        return
    for s in students:
        mark = float(input(f"  Mark of {s.get_name()}: "))
        s.set_mark(c.get_id(), mark)
 
 
def list_courses():
    print("--- Courses ---")
    for c in courses:
        c.list()
 
 
def list_students():
    print("--- Students ---")
    for s in students:
        s.list()
 
 
def show_marks():
    list_courses()
    c = find_course(input("Select course ID: "))
    if c is None:
        print("Course not found.")
        return
    print(f"--- Marks of {c.get_name()} ---")
    for s in students:
        print(f"{s.get_name():<20}{s.get_mark(c.get_id())}")
 
 
def main():
    while True:
        print("\n1. Input students")
        print("2. Input courses")
        print("3. Input marks")
        print("4. List courses")
        print("5. List students")
        print("6. Show marks")
        print("0. Exit")
        choice = input("Choice: ")
        if choice == "1":
            input_students()
        elif choice == "2":
            input_courses()
        elif choice == "3":
            input_marks()
        elif choice == "4":
            list_courses()
        elif choice == "5":
            list_students()
        elif choice == "6":
            show_marks()
        elif choice == "0":
            break
 
 
main()