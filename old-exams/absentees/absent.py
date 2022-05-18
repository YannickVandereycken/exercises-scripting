import sys


with open("all.txt") as all:
    student = all.read().lower().splitlines()

with open("attending.txt") as attending:
    goodstudents = attending.read().lower().splitlines()

# absent = student
with open("absentees.txt","w") as absentees:
    for s in student:
        if s not in goodstudents:
            # print(s)
            absentees.write(s+"\n")

# print(student)
# print(goodstudents)
# print(absent)
