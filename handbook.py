"""
Inside conditions.json, you will see a subset of UNSW courses mapped to their 
corresponding text conditions. We have slightly modified the text conditions
to make them simpler compared to their original versions.

Your task is to complete the is_unlocked function which helps students determine 
if their course can be taken or not. 

We will run our hidden tests on your submission and look at your success rate.
We will only test for courses inside conditions.json. We will also look over the 
code by eye.

NOTE: We do not expect you to come up with a perfect solution. We are more interested
in how you would approach a problem like this.
"""
import json
import re

# NOTE: DO NOT EDIT conditions.json
with open("./conditions.json") as f:
    CONDITIONS = json.load(f)
    f.close()


class Variable:
    def __init__(self, course, courses_list):
        this.course = course
        this.course_list = course_list

    def search():
        if course in course_list:
            return True 
        return False

class Operator:
    def __init__(self, left, right, operator):
        self.left = left
        self.right = right
        self.operator = operator
        self.courses = courses_list

    def recurse():
        result1 = result2 = True
        if (isinstance(left, Operator)):
            result1 = left.recurse()
        
        if (isinstance(right, Operator)):
            result2 = right.recurse()

        if (isinstance(left, Variable)):
            result1 = left.search()

        if (isinstance(right, Variable)):
            result2 = right.search()
        
        if (operator == "AND")
            return result1 and result2 
        
        if (operator == "OR")
            return result1 or result2
        

def splitBracket(courses, inputString):
    word = []
    brackets = False
    for i in (inputString + " "):
        if i == " " and brackets == False:
            str1 = ''.join(word)
            courses.append(str1.strip())
            word = []
        elif i == "(":
            brackets = True
        elif i == ")":
            brackets = False
        else: 
            word.append(i)

def split(courses, inputString):
    word = []
    brackets = False
    for i in (inputString + " "):
        if i == " " and brackets == False:
            str1 = ''.join(word)
            courses.append(str1.strip())
            word = []
        elif i == "(":
            brackets = True
        elif i == ")":
            brackets = False 
        word.append(i)
 

def search(courses_list, prereq):
    for i in range(1, len(courses_list)):
        if prereq[i] == "AND" or prereq[i] == "OR"
        
    print(f"{prereq}")



def is_unlocked(courses_list, target_course):
    """Given a list of course codes a student has taken, return true if the target_course 
    can be unlocked by them.
    
    You do not have to do any error checking on the inputs and can assume that
    the target_course always exists inside conditions.json

    You can assume all courses are worth 6 units of credit
    """
    
    # TODO: COMPLETE THIS FUNCTION!!!
    redundant_word = ["PREREQUISITE:", "PRE-REQUISITE:", "PRE-REQ:", "OF" ,"CREDIT", "IN"]
    

    #Set to upper string
    requiredCourses = CONDITIONS[target_course].upper()
    
    for i in redundant_word:
        requiredCourses = requiredCourses.replace(i, "")
    requiredCourses = requiredCourses.strip()
    courses = []
    split(courses, requiredCourses)
    search(courses_list, courses)

    return True 

def main():
    is_unlocked([], "COMP3900")

if __name__ == "__main__":
    main()




    