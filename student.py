import numpy as np


class Student:
    def __init__(self, sid, name, dob):
        self.__id = sid
        self.__name = name
        self.__dob = dob
        self.__marks = {}            # {course_id: mark}

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

    def __str__(self):
        return f"{self.__id:<8}{self.__name:<20}{self.__dob}"
