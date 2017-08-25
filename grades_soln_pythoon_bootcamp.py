# Given:

from pprint import pprint
import statistics as stats

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

# 1. Create a dict mapping names to lists of grades.
# Version 1 - imperative
print("1: name2grades")
name2grades = {}
for grade_line in grades[1:]:
    name2grades[grade_line[0]] = [int(x) for x in grade_line[1:]]
pprint(name2grades)

# 1A. Using comprehensions
print("1: name2grades2")
name2grades2 = {grade_line[0]: [int(x) for x in grade_line[1:]]
                for grade_line in grades[1:]}
pprint(name2grades2)

#1B. Dict mapping names to their lowest grades
print("1B: name2lowest_grade")
name2lowest_grade = {grade_line[0]: min([int(x) for x in grade_line[1:]])
                     for grade_line in grades[1:]}
pprint(name2lowest_grade)


# 1C. For Farva, create and print a list containing "Pass" for grades
# above 59, "Fail" otherwise

farva_grades = name2grades['Farva']
farva_fails = ["Pass" if grade > 59 else "Fail" for grade in farva_grades]
print("1C: farva_fails")
pprint(farva_fails)

# 2. Create a dict mapping names to dictionaries of grades.
# Ex: {'Thorny': {'Exam 1': '100', 'Exam 2': '90', 'Exam 3': '80'}}
print("2: name2grades4")
name2grades3 = {}
for line in grades[1:]:
    grades_dict = {}
    for i, grade in enumerate(line[1:]):
        grades_dict[grades[0][i + 1]] = grade
    name2grades2[line[0]] = grades_dict
pprint(name2grades2)
print("Foster's exam 2 score: ", name2grades2['Foster']['Exam 2'])

# 2A. Using comprehensions
name2grades4 = {line[0]: {grades[0][i + 1]: grade
                          for i, grade in enumerate(line[1:])}
                for line in grades[1:]}
print("2A: name2grades4")
pprint(name2grades4)

# 3. Create a dict mapping names to grade averages.
name2avg = {}
for line in grades[1:]:
    name2avg[line[0]] = stats.mean([int(x) for x in line[1:]])

print("3: name2avg")
pprint(name2avg)


# 4. Create a dict mapping items to average for that item across all students.
item2avg = {}
for i, item in enumerate(grades[0][1:]):
    itemgrades = []
    for line in grades[1:]:
        itemgrades.append(int(line[i+1]))
    item2avg[item] = stats.mean(itemgrades)

print("4: item2avg")
pprint(item2avg)

# 5. Sort the students by their grades on Exam 1

def by_exam1(grades_line):
    return int(grades_line[1])

print("5: Sort by grades on Exam 1")
pprint(sorted(grades[1:], key=by_exam1, reverse=True))

print("5A: Sort by grades on Exam 1 using lamba fn")
pprint(sorted(grades[1:], key=lambda line: int(line[1]), reverse=True))


# 6. Sort the students by their grade averages.
def grade_average(grade_line):
    return name2avg[grade_line[0]]

print("6: Sort by grade averages")
pprint(sorted(grades[1:], key=grade_average, reverse=True))

# 6A. Same as above, but not using the names2avgs dict or a named function

print("6A: Sort by grade averages using lambda fn")
pprint(sorted(grades[1:],
              key=lambda line: stats.mean([int(grade) for grade in line[1:]]),
              reverse=True))



# 7. Which student has the highest average?

print("7: Student with highest average")
pprint(max(grades[1:],
           key=lambda line: stats.mean([int(grade) for grade in line[1:]])))
