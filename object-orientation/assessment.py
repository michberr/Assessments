"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   Encapsulation: In oo-programming, the data lives close to its functionality, 
   i.e. specific methods are defined for specific classes of objects.

   Abstraction: OO-programming hides away some of the complexity of a program. 
   For example, you don't need to understand every method if you understand
   generally what a class entails. 

   Polymorphism: Ability to use a common interface for objects, despite them
   being derived from different classes. For example, you can have a "speak"
   method for both cat and dog objects that returns the appropriate animal noise
   without needing to write cat_speak and dog_speak functions. This is often made 
   possible through method inheritance. 


2. What is a class?
A class comprises the defining features of an object. Classes can have 
attributes and functions (called methods) which apply to each instance of a class.
Ultimately, classes are a way to organize code in a hierarchical fashion, so that 
similar objects have the same defining features, and can inherit other features from 
higher-level classes.
 

3. What is an instance attribute?
It's an attribute that is specific to an instance (rather than its class). If you 
change an attribute on an instance, it does not affect any other instances or
instances-to-be. 

4. What is a method?
A method is a function defined for a class. Methods are called on instances of 
the class they were defined for.

5. What is an instance in object orientation?
An instance is an occurence of a class that occupies its own space in memory. 
One can create several instances of the same class that often share some attributes
and will share the methods they have access to.

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.
A class attribute is true for all instances of a class. An instance attribute 
is only true for a single instance. 

For example, if we made a class called GraceStudents, it might have class 
attributes of cohort = Grace and instructors = ['Bonnie', 'Henry'], 
but each instance will have its own attributes for student_name, student_project, etc. 


"""


# Parts 2 through 5:
# Create your classes and class methods

class Student(object):
    """Class for holding student id information"""

    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

class Question(object):
    """Class to create questions and evaluate their answers"""

    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):
        """Determines if user answered question correctly"""

        print self.question
        user_answer = raw_input("> ")
        return user_answer == self.correct_answer


class Exam(object):
    """Exams hold questions and administer tests"""
  
    def __init__(self, name):
        self.name = name
        self.questions = []


    def add_question(self, question, correct_answer):
        """Add question to exam"""
        q = Question(question, correct_answer)
        self.questions.append(q)

    def administer(self):
        """Administers exam, and returns score as percentage points"""

        score = 0

        for question in self.questions:
            # Loop through each question in exam, and add to score
            # if a question is correct
            if question.ask_and_evaluate():
                score += 1

        # return student score as a percentage
        return (float(score)/len(self.questions)) * 100

class Quiz(Exam):
    """Quizzes are like exams, but are only pass/fail"""

    def administer(self):
        """If student scored 50 or above, they pass"""

        score = super(Quiz, self).administer()
        
        if score >= 50:
            return True
        else:
            return False


def take_test(exam, student):
    """Administer an exam on a student and print their score"""

    student.score = exam.administer()

    print "{} {}'s score was {}".format(student.first_name, student.last_name, student.score)

def example():
    """An example exam administered on a student."""

    # Create exam
    exam = Exam("Hard Exam")

    # Add questions to exam
    exam.add_question("What is 15/5?", "3")
    exam.add_question("What is 4*30", "120")
    exam.add_question("What is the capital of France", "Paris")
    exam.add_question("How many days are there in a year?", "365")

    # Create student
    student = Student("Michelle", "Berry", "123 1st St")

    # Administer test to student
    take_test(exam, student)

