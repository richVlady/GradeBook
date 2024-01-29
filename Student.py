# create the profile for each student.
# store their AVG, each assesment grade, ext

class Student:
    def __init__(self, name, tW, qW):
        self.name = name
        self.AVGs = []
        self.testGrades = []
        self.quizGrades = []
        self.testWeight = tW
        self.quizWeight = qW

    def getName(self):
        return self.name

    def tests(self,allTests):
        self.testGrades = allTests

    def quizzes(self, allQuiz):
        self.quizGrades = allQuiz

    def calcAVGs(self, bonus):
        tTotal = 0
        qTotal = 0
        self.AVGs.clear()
        for x in self.testGrades:
            tTotal += int(x)
        self.AVGs.append(tTotal/len(self.testGrades))

        for y in self.quizGrades:
            qTotal += int(y)
        self.AVGs.append(qTotal/len(self.quizGrades))

        TAvg = round((self.AVGs[0]*(self.testWeight/100.0) + self.AVGs[1]*(self.quizWeight/100.0)),2)
        if TAvg+int(bonus) >= 100:
            self.AVGs.append(100)
        else:
            self.AVGs.append(TAvg+int(bonus))
        return self.AVGs

    def report(self):
        print("-----------------------------------------")
        print("Test Grades:")
        for x in range (0,len(self.testGrades)):
            print("\tTest #" + str(x) + ": " + str(self.testGrades[x]))
        print("Quiz Grades:")
        for x in range(0, len(self.quizGrades)):
            print("\tQuiz #" + str(x) + ": " + str(self.quizGrades[x]))

        print("\t\tTest Average: " + str(self.AVGs[0]))
        print("\t\tQuiz Average: " + str(self.AVGs[1]))
        print("\t\tOverall Average: " + str(self.AVGs[2]))
        print("-----------------------------------------")










