import curses
import math
from domains import Student, Course


def ask(scr, prompt):
    scr.addstr(prompt)
    curses.echo()
    text = scr.getstr().decode().strip()
    curses.noecho()
    return text


def ask_int(scr, prompt):
    while True:
        try:
            n = int(ask(scr, prompt))
            if n > 0:
                return n
            scr.addstr("Please enter a positive number.\n")
        except ValueError:
            scr.addstr("Invalid number, try again.\n")


def input_students(scr, students):
    n = ask_int(scr, "Number of students: ")
    for i in range(n):
        scr.addstr(f"Student {i + 1}:\n")
        sid = ask(scr, "  ID: ")
        name = ask(scr, "  Name: ")
        dob = ask(scr, "  Date of birth: ")
        students.append(Student(sid, name, dob))


def input_courses(scr, courses):
    n = ask_int(scr, "Number of courses: ")
    for i in range(n):
        scr.addstr(f"Course {i + 1}:\n")
        cid = ask(scr, "  ID: ")
        name = ask(scr, "  Name: ")
        credit = ask_int(scr, "  Credit: ")
        courses.append(Course(cid, name, credit))


def input_marks(scr, students, course):
    for s in students:
        while True:
            try:
                mark = float(ask(scr, f"  Mark of {s.get_name()}: "))
                break
            except ValueError:
                scr.addstr("  Invalid mark.\n")
        mark = math.floor(mark * 10) / 10
        s.set_mark(course.get_id(), mark)
