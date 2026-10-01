import curses
import input as inp
import output as out

students = []
courses = []


def find_course(cid):
    for c in courses:
        if c.get_id() == cid:
            return c
    return None


def find_student(sid):
    for s in students:
        if s.get_id() == sid:
            return s
    return None


def main(scr):
    out.init_colors()
    while True:
        out.print_menu(scr)
        choice = inp.ask(scr, "Choice: ")
        if choice == "0":
            break
        elif choice == "1":
            out.title(scr, "INPUT STUDENTS")
            inp.input_students(scr, students)
        elif choice == "2":
            out.title(scr, "INPUT COURSES")
            inp.input_courses(scr, courses)
        elif choice == "3":
            out.title(scr, "INPUT MARKS")
            out.print_courses(scr, courses)
            c = find_course(inp.ask(scr, "\nSelect course ID: "))
            if c is None:
                scr.addstr("Course not found.\n")
            else:
                inp.input_marks(scr, students, c)
        elif choice == "4":
            out.title(scr, "COURSES")
            out.print_courses(scr, courses)
        elif choice == "5":
            out.title(scr, "STUDENTS")
            out.print_students(scr, students)
        elif choice == "6":
            out.title(scr, "SHOW MARKS")
            out.print_courses(scr, courses)
            c = find_course(inp.ask(scr, "\nSelect course ID: "))
            if c is None:
                scr.addstr("Course not found.\n")
            else:
                out.print_marks(scr, students, c)
        elif choice == "7":
            out.title(scr, "STUDENT GPA")
            s = find_student(inp.ask(scr, "Student ID: "))
            if s is None:
                scr.addstr("Student not found.\n")
            else:
                out.print_gpa(scr, s, courses)
        elif choice == "8":
            out.title(scr, "STUDENTS SORTED BY GPA (DESC)")
            students.sort(key=lambda s: s.get_gpa(courses), reverse=True)
            out.print_gpa_ranking(scr, students, courses)
        else:
            continue
        out.pause(scr)


curses.wrapper(main)
