class Student:

    def __init__(self, name, hours, qpoints):
        self.name = name
        self.hours = float(hours)
        self.qpoints = float(qpoints)

    def getName(self):
        return self.name

    def getHours(self):
        return self.hours

    def getQPoints(self):
        return float(self.qpoints)

    def addPointsAndHours(self, gpoints, extra_hours):
        self.hours = float(self.hours + extra_hours)
        self.qpoints = float(self.qpoints + extra_hours*gpoints)

    def gpa(self):
        return float(self.qpoints / self.hours)


john = Student("John", 0, 0)
for i in range(3):
    grade = float(input("Grade (A=4, B=3, C=2, D=1, F=0): "))
    credits = float(input("Credit hours: "))
    john.addPointsAndHours(grade, credits)
    print("Student:", john.getName(), " Grade Points:", john.getQPoints(), " Total Hours:", john.getHours(), " GPA:", "%.2f" % john.gpa())