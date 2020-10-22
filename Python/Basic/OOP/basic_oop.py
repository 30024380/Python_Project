# Basic OOP 

# Student Class
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade 
    
    # Method
    def get_grade(self):
        return self.grade
# Class
class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        # Making a blank list
        self.students = []

    # Method that allows us to add students to the blank list
    def add_students(self, student):
        # Only add students if its less then the max amount of students in the course
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    
    # Method that calculates the average grade between students
    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()

        return value /len(self.students)
        

# Making the students
s1 = Student("Tim", 19, 95)
s2 = Student("Todd", 19, 75)
s3 = Student("Terry", 19, 55)

# Making the course
course = Course("Science", 2)

# Adding students to a course
course.add_students(s1)
course.add_students(s2)

# Printing student name and calling the average grade method
print(course.students[0].name)
print(course.students[1].name)
print(course.get_average_grade())