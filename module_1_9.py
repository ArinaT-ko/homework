grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

l_students = list(students)
l_students.sort()

result = {}

for i in range(len(l_students)):
    result[l_students[i]] = round(sum(grades[i])/ len(grades[i]), 2)

print(result)

