# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 16:38:36 2017

@author: yan.yl.chen
"""

# Given:

grades = [
    # First line is descriptive header. Subsequent lines hold data
    ['Student', 'Exam 1', 'Exam 2', 'Exam 3'],
    ['Thorny', '100', '90', '80'],
    ['Mac', '88', '99', '111'],
    ['Farva', '45', '56', '67'],
    ['Rabbit', '59', '61', '67'],
    ['Ursula', '73', '79', '83'],
    ['Foster', '89', '97', '101']
]

# Create a dict mapping names to lists of grades.
grade_dict1 = {}
for student_grade in grades[1:]:
    grade_list =[]
    for i in range (1,4):
        grade_list.append(int(student_grade[i]))
    grade_dict1[student_grade[0]] = grade_list

#print(grade_dict1)

# Create a dict mapping names to dicitonaries of grades.
grade_dict2 = {}
for student_grade in grades[1:]:
   student_grade_dict = {}
   for i in range(1,4):
        student_grade_dict["Exam " + str(i)] = student_grade[i]
   grade_dict2[student_grade[0]] = student_grade_dict
             
#print(grade_dict2)        
        
# Create a dict mapping names to grade averages.
avg_grade_dict = {}
for (name, grade_list) in grade_dict1.items():
    avg_grade = sum(grade_list) / len(grade_list)
    avg_grade_dict[name] = avg_grade
    
#print(avg_grade_dict)
    

# Create a dict mapping items to average for that item across all students.
total_avg_dict = {}

for i in range (1,4):
   total_grade = 0
   people_count = 0
   for grade_list in grade_dict1.values():
       total_grade += grade_list[i-1]
       people_count +=1
   avg_grade = total_grade / people_count
   
   total_avg_dict["Exam " + str(i)] = avg_grade
   
#print(total_avg_dict)

# Sort the students by their grades on Exam 1

exam1_list = []
for (name, grade_list) in grade_dict1.items():
    exam1_list.append((grade_list[0], name))

exam1_list.sort()
print(exam1_list)

# Sort the students by their grade averages.
avg_grade_list = []
for (name, grade_list) in grade_dict1.items():
    avg_grade = sum(grade_list) / len(grade_list)
    avg_grade_list.append((avg_grade, name))

avg_grade_list.sort()
print(avg_grade_list)

# Which student has the highest average?
avg_grade_list.reverse()
print(avg_grade_list[0][1])


