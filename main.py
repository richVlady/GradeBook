# GradeBook
# runner program
# inputs of grades into single list of students
# allow user to extract data

from Student import Student
import copy

# collect starting data to create overall gradebook
print("Welcome to your gradebook!")
numStudents = int(input("How many student are in your class?"))
tW = int(input("What percent of the total grade do the Tests account for?"))
qW = int(input("What percent of the total grade do the Quizzes account for?"))
numTests = int(input("How many tests are there?"))
numQuiz = int(input("How many quizzes are there?"))

# create list variables
students = []
testGrades = []
quizGrades = []

# for loop to fill the grade for each students
for x in range (0,numStudents):
    testGrades.clear()
    quizGrades.clear()

    name = input("What is the name of student #" + str(x) + ": ")
    students.append(Student(name,tW,qW))

    print("Enter the grade that the student received on each of their tests.")
    for testNum in range (0,numTests):
        testGrade = int(input("Grade on test #" + str(testNum+1) + ":"))
        testGrades.append(testGrade)

    print("Enter the grade that the student received on each of their quizzes.")
    for quizNum in range (0,numQuiz):
        quizGrade = int(input("Grade on quiz #" + str(quizNum+1) + ":"))
        quizGrades.append(quizGrade)

    students[x].tests(copy.deepcopy(testGrades))
    students[x].quizzes(copy.deepcopy(quizGrades))
    print("----------------------------------------------------")

# print the names and roster before awarding bonus points
print("Name:\t\t\tGrade:")
for x in students:
    print(x.getName() + "\t\t\t" + str((x.calcAVGs(0))[2]))

# choose student to awards bonuns points to
bonName = input("Which student would you like to add a bonus to? (\"none\" for none)")
while bonName != "none":
    bonNum = input("How many bonus points to their Overall average?")
    for x in students:
        if x.getName().lower() == bonName.lower():
            x.calcAVGs(bonNum)
            bonName = input("Would you like to give another bonus? (give name,  \"none\" for none)")
            count = 1
            break
    if count != 1:
        str = input("No student has this name. Please enter a valid student.")


# allow use to pull data from chosen students
stu = input("Which student would you like to see the full grade report for? (\"none\" to exit)")
while stu != "none":
    for x in students:
        if x.getName().lower() == stu.lower():
            print(x.report())
            stu = input("Any other students? (enter name, \"none\" to exit)")
            count1 = 1
            break
    if count1 != 1:
        stu = input("No student has this name. Please enter a valid student.")






