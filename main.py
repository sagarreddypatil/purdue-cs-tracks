from util import Course, Track
from courselist import systems_track, mi_track

my_tracks = systems_track + mi_track

all_courses = {}
for track in my_tracks:
    for course in track.courses:
        if course not in all_courses:
            all_courses[course] = []
        all_courses[course].append(track)


for track in my_tracks:
    print(f"{track}")
    for course in track.courses:
        other_tracks = ",".join([other.name for other in all_courses[course] if other != track])
        print(f"\t{course} ({other_tracks})")
    print()
