from typing import Union


class Course:
    all_courses = {}

    def __init__(self, course: str, title: str):
        if course in Course.all_courses:
            raise ValueError(f"Course {course} already exists")

        self.course = course
        self.title = title

    @staticmethod
    def get_or_create(course: str, title: str):
        if course in Course.all_courses:
            return Course.all_courses[course]
        else:
            course_obj = Course(course, title)
            Course.all_courses[course] = course_obj
            return course_obj

    # @staticmethod
    # def from_tuple(t):
    #     return Course(t[0], t[1])

    def __hash__(self):
        return hash(self.course)

    def __str__(self):
        return f"{self.course} - {self.title}"

    def __repr__(self):
        return f"Course({self.course}, {self.title})"


class Track:
    def __init__(self, name: str):
        self.name = name
        self.courses = []

    def add_course(self, course: Course):
        self.courses.append(course)

    def add_courses(self, courses: list[Course]):
        self.courses += courses

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Track('{self.name}')"
