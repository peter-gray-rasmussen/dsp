the_list = sorted([5,4,3,2,1,4])
print the_list

a = [5,4,3,2,1]
a.sort()

print a

the_dict = sorted({1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'})

print the_dict

key_time = sorted ("This is a test string from Peter".split(), key=str.lower)
print key_time

student_tuples = [
        ('john', 'A', 15),
        ('jane', 'B', 12),
        ('dave', 'B', 10),
]

print student_tuples

student_tuples = sorted(student_tuples, key=lambda student: student[2]) # sort by age
print student_tuples
