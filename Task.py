
# Task  : 1
print("Task : 1")

input_str = "aaabbaacccaab"
print("Count letters in whole string : ",len(input_str))

print("")

from itertools import groupby
 
input_str = "aaabbaacccaab"

print("original string : " + input_str)
res = [len(list(j)) for _, j in groupby(input_str)]
print("Count consecutive letters in whole string : " + str(res))
print("-"*30)
print("")

# Task : 2

print("Task : 2")

input_list = [1, 2, 3, 4, 5]

print("Original List : ",input_list)
squ_list = [a**2 for a in input_list]
print("square List ", squ_list)

sum_square = sum(a**2 for a in input_list)
print("Sum of Square : ",sum_square)

print("-"*30)
print("")

# Task : 3

print("Task : 3")

def palidrome(input_string):
    if len(input_string) == 0 or len(input_string) == 1:
        return True

    for i in range(len(input_string) // 2):
        if input_string[i] != input_string[len(input_string) - 1 - i]:
            return False

    return True

print("Palindrome : ",palidrome("nayan"))
print("Not Palindrome : ",palidrome("hello"))

print("-"*30)
print("")

# Task : 4

print("Task : 4")

input_tuple_list = [(4,2,7),(3,4,8),(1,2,4),(7,6,1),(9,3,1),(2,4,2)]

print("Original List : ",input_tuple_list)


def last(n):
    return n[-1]  
  
def sort(tuples):
    return sorted(tuples, key=last)
  
input_tuple_list = [(4,2,7),(3,4,8),(1,2,4),(7,6,1),(9,3,1),(2,4,2)]
print("Sorted List : ",sort(input_tuple_list))

print("-"*30)
print("")

# Task : 5

print("Task : 5")

student_marks = {
  'Physics': 82,
  'Math': 65,
  'history': 75,
  'Ashok': 60,
  'Reddy': 60,
  'RRR': 50,
  'aaa': 50
}
print("Student Marks = ",student_marks)

second_high = sorted(set(student_marks.values()), reverse=True)[1]

second_high_students = [student for student, mark in student_marks.items() if mark == second_high]

print("Second Highiest Marks : ", second_high_students)

print("-"*30)
print("")


# Task : 6

print("Task : 6")
class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def compare(self, other):
        return self.__dict__ == other.__dict__

c1 = Vector(10, 20)
c2 = Vector(10, 20)

t_f = c1.compare(c2)

print(t_f)


print("-"*30)
print("")

# Task : 7

print("Task : 7")
def odd_even(input_list):
    result_dict = {'odd': set(), 'even': set()}

    for num in input_list:
        if num % 2 == 0:
            result_dict['even'].add(num)
        else:
            result_dict['odd'].add(num)

    return result_dict

input_list = [5, 8, 10, 13, 100, 104, 107, 13, 1031, 5, 1245, 1111, 10, 1031, 8, 1032]

res = odd_even(input_list)
print(res)

print("-"*30)
print("")

#Task : 8

print("Task : 8")
def squar(input_dict):
    return [value ** 2 for value in input_dict.values()]

def not_divide(input_list):
    return [value for value in input_list if value % 2 != 0]


input_dict = {"Total_classes": 2, "Total_students": 10}


s = squar(input_dict)
print(s)


no = not_divide(s)
print(no)



