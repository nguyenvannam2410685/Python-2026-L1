import curses


def init_colors():
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)


def title(scr, text):
    scr.clear()
    scr.addstr(text + "\n", curses.color_pair(1) | curses.A_BOLD)
    scr.addstr("=" * 45 + "\n\n", curses.color_pair(1))


def pause(scr):
    scr.addstr("\nPress any key to continue...", curses.color_pair(2))
    scr.getch()


def print_menu(scr):
    title(scr, "STUDENT MARK MANAGEMENT")
    scr.addstr("1. Input students\n")
    scr.addstr("2. Input courses\n")
    scr.addstr("3. Input marks\n")
    scr.addstr("4. List courses\n")
    scr.addstr("5. List students\n")
    scr.addstr("6. Show marks of a course\n")
    scr.addstr("7. Show GPA of a student\n")
    scr.addstr("8. Sort students by GPA\n")
    scr.addstr("0. Exit\n\n")


def print_courses(scr, courses):
    for c in courses:
        scr.addstr(str(c) + "\n")


def print_students(scr, students):
    for s in students:
        scr.addstr(str(s) + "\n")


def print_marks(scr, students, course):
    scr.addstr(f"\nMarks of {course.get_name()}:\n")
    for s in students:
        scr.addstr(f"{s.get_name():<20}{s.get_mark(course.get_id())}\n")


def print_gpa(scr, student, courses):
    scr.addstr(f"GPA of {student.get_name()}: {student.get_gpa(courses):.2f}\n")


def print_gpa_ranking(scr, students, courses):
    for s in students:
        scr.addstr(f"{s.get_id():<8}{s.get_name():<20}{s.get_gpa(courses):.2f}\n")
