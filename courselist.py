from util import Track, Course


def parse_courses(course_string: str) -> list[Course]:
    course_list = []
    for line in course_string.splitlines():
        course_list.append(Course.get_or_create(*line.split("\t")))
    return course_list


systesm_core = """CS 35200	Compilers: Principles and Practice
CS 35400	Operating Systems
CS 42200	Computer Networks"""

systems_electives = """CS 30700	Software Engineering I
CS 33400	Fundamentals of Computer Graphics
CS 35300	Principles of Concurrency and Parallelism
CS 38100	Introduction to the Analysis of Algorithms
CS 42600	Computer Security
CS 44800	Introduction to Relational Database Systems
CS 45600	Programming Languages
CS 48900	Embedded Systems
CS 49000 DS0	Distributed Systems"""

mi_core = """CS 37300	Data Mining and Machine Learning
CS 38100	Introduction to the Analysis of Algorithms
CS 47100	Artifical Intelligence
STAT 41600	Probability"""

mi_electives = """CS 34800	Information Systems
CS 35200	Compilers: Principles And Practice
CS 44800	Introduction To Relational Database Systems
CS 45600	Programming Languages
CS 47100	Introduction to Artificial Intelligence
CS 48300	Introduction To The Theory Of Computation
CS 47300	Web Information Search & Management"""

seng_core = """CS 30700	Software Engineering I	
CS 35200	Compilers: Principles and Practice 	
CS 35400	Operating Systems	
CS 38100	Introduction to the Analysis of Algorithms	
CS 40800	Software Testing	
CS 40700	Software Engineering Senior Project"""

seng_electives = """CS 34800	Information Systems
CS 35200	Compilers: Principles and Practice
CS 35300	Principles of Concurrency and Parallelism
CS 35400	Operating Systems
CS 37300	Data Mining and Machine Learning
CS 42200	Computer Networks
CS 42600	Computer Security
CS 44800	Introduction to Relational Database Systems
CS 45600	Programming Languages
CS 47300	Web Information Search And Management
CS 48900	Embedded Systems
CS 49000-CLC	Cloud Computing
CS 49000-DSO	Distributed Systems
CS 49000-SWS	Software Security
CS 51000	Software Engineering
CS 59000-SRS	Software Reliability and Security"""

systems_core_track = Track("Systems Core")
systems_elective_track = Track("Systems Elective")

mi_core_track = Track("Machine Intelligence Core")
mi_elective_track = Track("Machine Intelligence Elective")

seng_core_track = Track("Software Engineering Core")
seng_elective_track = Track("Software Engineering Elective")


systems_core_track.add_courses(parse_courses(systesm_core))
systems_elective_track.add_courses(parse_courses(systems_electives))

mi_core_track.add_courses(parse_courses(mi_core))
mi_elective_track.add_courses(parse_courses(mi_electives))

seng_core_track.add_courses(parse_courses(seng_core))
seng_elective_track.add_courses(parse_courses(seng_electives))

systems_track = [systems_core_track, systems_elective_track]
mi_track = [mi_core_track, mi_elective_track]
seng_track = [seng_core_track, seng_elective_track]
