'''
Class that defines a student object with full name, graduation year, trico college and dunctionalities for course list.
Author: Aaryaman Jaising
Date: January 21, 2025
'''

class Student:

    """ ========== TODO : START ========== """

    """TODO: Create a constructor."""
    def __init__(self,name,grad_year,college):
        self.name = name
        self.grad_year = grad_year
        self.college = college
        self.course_list = []
        pass

    """TODO: Write the add course method"""
    def add_course(self,course):
        """
        course: course name to add to course list
        prints whether course was added or not if it already was in the list.
        """
        if course in self.course_list:
            print(f"Student is already taking course: {course}")
        else:
            self.course_list.append(course)
            print(f"Course added to course list: {course}")

    """TODO: Write the drop course method"""
    def drop_course(self,course):
        """
        course: course name to delete from course list
        prints whether course was deleted or not if it already was not in the list.
        """
        if course not in self.course_list:
            print(f"Course is not in the student's list: {course}")
        else:
            self.course_list.remove(course)
            print(f"Course was dropped from list: {course}")

    """TODO: Write the __str__ method"""
    def __str__(self):
        return f"Name: {self.name}\nGraduation Year: {self.grad_year}\nCollege Name: {self.college}\nCourse List: {self.course_list}"
        pass

    """ ========== TODO : END ========== """

def main():

    """ ========== TODO : START ========== """
    """TODO: Create an instance of Student and test all the methods"""

    print("Student Class Testing\n")
    # TODO create instance
    student1 = Student("Aaryaman Jaising",2026,"Haverford College")
    print("\nTesting add_course and drop_course:")
    # TODO test add/drop
    student1.add_course("Multivariate Statistics")
    student1.add_course("Data Science")
    student1.add_course("Data Science")
    student1.drop_course("Math")
    student1.drop_course("Multivariate Statistics")

    print("\nTest __str__:")
    # TODO test __str__
    print(student1)

    student_lst = [["Fiona Xu", 2026, "Haverford College"],
                   ["Ivy Zhang", 2024, "Bryn Mawr College"],
                    ["Alton Wiggers", 2025, "Swarthmore College"],
                    ["Luis Contreras-Orendain", 2023, "Haverford College"],
                    ["Lizzie Spano", 2023, "Bryn Mawr College"]]

    print('\n')
    print("Student Dictionary Exercises\n")
    # TODO create dictionary called students
    students = {}
    for i,lst in enumerate(student_lst):
        students[i] = Student(lst[0],lst[1],lst[2])

    print("Dictionary contents:")
    print_dict(students)

    print("Trying to add a student with same key:")
    # TODO
    lst = student_lst[0]
    students[1] = Student(lst[0],lst[1],lst[2])

    print("Dictionary contents afterwards:")
    print_dict(students)

    print("Trying to add a student with new key and a repeated value/Student:")
    # TODO
    students[5] = Student(lst[0],lst[1],lst[2])
    print("Dictionary contents afterwards:")
    print_dict(students)

    specific_id = 1 # TODO
    print("Getting Student at key %i:" % (specific_id))
    # TODO
    print(students[specific_id])
    print("Removing Student at key %i:" % (specific_id))
    students.pop(specific_id)
    print("Dictionary contents afterwards:")
    print_dict(students)

    """ ========== TODO : END ========== """


def print_dict(dictionary):
    """Function that prints out the keys and values in a dictionary"""
    for key, val in dictionary.items():
        print(key, val)


if __name__ == "__main__":
    main()
