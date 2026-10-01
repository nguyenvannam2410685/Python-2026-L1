import curses
import math
import numpy as np
 
 
class Student:
    def __init__(self):
        self.__id = ""
        self.__name = ""
        self.__dob = ""
        self.__marks = {}          
 
    def get_id(self):
        return self.__id
 
    def get_name(self):
        return self.__name
 
    def set_mark(self, course_id, mark):
        self.__marks[course_id] = mark
 
    def get_mark(self, course_id):
        return self.__marks.get(course_id, "N/A")
 
    def get_gpa(self, courses):
        marks = []
        credits = []
        for c in courses:
            if c.get_id() in self.__marks:
                marks.append(self.__marks[c.get_id()])
                credits.append(c.get_credit())
        if len(credits) == 0:
            return 0.0
        marks = np.array(marks)
        credits = np.array(credits)
        return float(np.sum(marks * credits) / np.sum(credits))
 
    def input(self, scr):
        scr.addstr("  ID: ")
        self.__id = scr.getstr().decode()
        scr.addstr("  Name: ")
        self.__name = scr.getstr().decode()
        scr.addstr("  Date of birth: ")
        self.__dob = scr.getstr().decode()
 
    def list(self, scr):
        scr.addstr(f"{self.__id:<8}{self.__name:<20}{self.__dob}\n")
 
 
class Course:
    def __init__(self):
        self.__id = ""
        self.__name = ""
        self.__credit = 0
 
    def get_id(self):
        return self.__id
 
    def get_name(self):
        return self.__name
 
    def get_credit(self):
        return self.__credit
 
    def input(self, scr):
        scr.addstr("  ID: ")
        self.__id = scr.getstr().decode()
        scr.addstr("  Name: ")
        self.__name = scr.getstr().decode()
        scr.addstr("  Credit: ")
        self.__credit = int(scr.getstr().decode())
 
    def list(self, scr):
        scr.addstr(f"{self.__id:<8}{self.__name:<20}{self.__credit} credit(s)\n")
 
 
students = []
courses = []
 
 
def input_students(scr):
    scr.addstr("Number of students: ")
    n = int(scr.getstr().decode())
    for i in range(n):
        scr.addstr(f"Student {i + 1}:\n")
        s = Student()
        s.input(scr)
        students.append(s)
 
 
def input_courses(scr):
    scr.addstr("Number of courses: ")
    n = int(scr.getstr().decode())
    for i in range(n):
        scr.addstr(f"Course {i + 1}:\n")
        c = Course()
        c.input(scr)
        courses.append(c)
 
 
def list_courses(scr):
    scr.addstr("--- Courses ---\n", curses.color_pair(1))
    for c in courses:
        c.list(scr)
 
 
def list_students(scr):
    scr.addstr("--- Students ---\n", curses.color_pair(1))
    for s in students:
        s.list(scr)
 
 
def find_course(cid):
    for c in courses:
        if c.get_id() == cid:
            return c
    return None
 
 
def input_marks(scr):
    list_courses(scr)
    scr.addstr("Select course ID: ")
    c = find_course(scr.getstr().decode())
    if c is None:
        scr.addstr("Course not found.\n")
        return
    for s in students:
        scr.addstr(f"  Mark of {s.get_name()}: ")
        mark = float(scr.getstr().decode())
        mark = math.floor(mark * 10) / 10     
        s.set_mark(c.get_id(), mark)
 
 
def show_marks(scr):
    list_courses(scr)
    scr.addstr("Select course ID: ")
    c = find_course(scr.getstr().decode())
    if c is None:
        scr.addstr("Course not found.\n")
        return
    scr.addstr(f"--- Marks of {c.get_name()} ---\n", curses.color_pair(1))
    for s in students:
        scr.addstr(f"{s.get_name():<20}{s.get_mark(c.get_id())}\n")
 
 
def show_gpa(scr):
    scr.addstr("Student ID: ")
    sid = scr.getstr().decode()
    for s in students:
        if s.get_id() == sid:
            scr.addstr(f"GPA of {s.get_name()}: {s.get_gpa(courses):.2f}\n")
            return
    scr.addstr("Student not found.\n")
 
 
def sort_by_gpa(scr):
    students.sort(key=lambda s: s.get_gpa(courses), reverse=True)
    scr.addstr("--- Students sorted by GPA ---\n", curses.color_pair(1))
    for s in students:
        scr.addstr(f"{s.get_name():<20}{s.get_gpa(courses):.2f}\n")
 
 
def main(scr):
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.echo()
    while True:
        scr.clear()
        scr.addstr("===== STUDENT MARK MANAGEMENT =====\n", curses.color_pair(1) | curses.A_BOLD)
        scr.addstr("1. Input students\n")
        scr.addstr("2. Input courses\n")
        scr.addstr("3. Input marks\n")
        scr.addstr("4. List courses\n")
        scr.addstr("5. List students\n")
        scr.addstr("6. Show marks of a course\n")
        scr.addstr("7. Show GPA of a student\n")
        scr.addstr("8. Sort students by GPA\n")
        scr.addstr("0. Exit\n")
        scr.addstr("Choice: ")
        choice = scr.getstr().decode()
 
        scr.clear()
        if choice == "0":
            break
        elif choice == "1":
            input_students(scr)
        elif choice == "2":
            input_courses(scr)
        elif choice == "3":
            input_marks(scr)
        elif choice == "4":
            list_courses(scr)
        elif choice == "5":
            list_students(scr)
        elif choice == "6":
            show_marks(scr)
        elif choice == "7":
            show_gpa(scr)
        elif choice == "8":
            sort_by_gpa(scr)
        scr.addstr("\nPress any key to go back...")
        scr.getch()
 
 
curses.wrapper(main)