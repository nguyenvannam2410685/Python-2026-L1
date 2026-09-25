class Student:
    def __init__(self,sid,name,dob):
        self.id=sid
        self.name=name
        self.dob=dob
    def __str__(self):
        return f"{self.id:<6}{self.name:<25}{self.dob}"

class Course:
    def __init__(self,id,name):
        self.id=id
        self.name=name
    def __str__(self):
        return f"{self.id:<6}{self.name:<25}"

students=[]
courses=[]
mark={}

def input_number_student():
    while True:
        try:
            n=int(input("ENTER NUMBER OF STUDENTS: "))
            if (n<=0):
                print("PLEASE ENTER POSITIVE NUMBER")
                continue
            return n
        except ValueError:
            print("Invalied try again")

def input_info_students():
    n=input_number_student()
    for s in range(n):
        print("\n----Student{0}-----".format(s+1))
        sid=input("-ID:").strip()
        name=input("-NAME:").strip()
        dob=input("-DOB:").strip()
        students.append(Student(sid,name,dob))
        mark[sid]={}

def input_number_course():
    while True:
        try:
            n=int(input("ENTER NUMBER OF COURSES:"))
            if(n<=0):
                print("PLEASE ENTER POSITIVE NUMBER")
                continue
            return n
        except ValueError:
            print("Invalied try again")

def input_info_courses():
    n=input_number_course()
    for c in range(n):
        print("-----Course{0}-----".format(c+1))
        id=input("-ID:").strip()
        name=input("-NAME:").strip()
        courses.append(Course(id,name))

def find_student_by_ID(sid):
    for s in students:
        if s.id==sid:
            return s 
    print("Not find student ID")

def find_courses_by_ID(cid):
    for c in courses:
        if c.id==cid:
            return c 
    print("Not find course ID")

def list_courses():
    if not courses:
        print("Not courrse")
        return
    print("%-12s%-25s"%("ID","NAME"))
    print("-"*37)
    for c in courses:
        print(f"{c.id:<12}{c.name:<25}")
    print()

def list_students():
    if not students:
        print("Not students")
        return
    print("%-12s%-25s%s"%("ID","NAME","DOB"))
    print("-"*37)
    for s in students:
        print(f"{s.id:<6}{s.name:<25}{s.dob}")
    print()

def select_mark_for_students():
    if not courses:
        print("Not course please course first")
        return
    if not students:
        print("Not find student")
        return
    list_courses()
    cid=input("Enter ID coursr to select mark:")
    course=find_courses_by_ID(cid)
    if course is None:
        print("Not coures please enter course first")
        return
    for s in students:
        while True:
            try:
                m=float(input(f"Mark of {course.name} for {s.name} ({s.id}):"))
                if 0<=m<=20:
                    break
            except ValueError:
                print("Invalied try agian ")
        mark[s.id][cid]=m

def show_mark_student():
    if not courses:
        print("Not find course")
        return
    list_courses()
    cid =input("Enter ID course to show:")
    course=find_courses_by_ID(cid)
    if course is None:
        print("Not find course try again")
        return
    list_students()
    sid=input("Enter student ID you want to show mark:")
    student=find_student_by_ID(sid)
    if student is None:
        print("Not find student to show mark,try again")
        return
    print(f"Mark for course {course.name}:")
    print("%-12s%-25s%s" % ("ID","NAME","MARK"))
    print("-"*30)
    for s in student:
        m=mark.get(student.id,{}).get(course.id,"N/A")
        print(f"{student.id:<6}{student.name:<25}{m}")
    print()

MENU="""
=========MENU=========
1,Input student information:id,name,DoB
2,Input course information:id,name
3,List courses
4,List students
5,Select a course,input marks for student in this class
6,Show student marks for a given course
7,Exit program
=======================
"""
def main():
    while True:
        print(MENU)
        n=input("Enter your choose:").strip()
        if n=="1":
            input_info_students()
        elif n=="2":
            input_info_courses()
        elif n=="3":
            list_courses()
        elif n=="4":
            list_students()
        elif n=="5":
            select_mark_for_students()
        elif n=="6":
            show_mark_student()
        elif n=="7":
            print("GOODBYE")
            break
if __name__=="__main__":
    main()