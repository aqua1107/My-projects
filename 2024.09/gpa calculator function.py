def get_grade(grade):
    grades = {'A+':4.5, 'A':4.0, 'B+':3.5, 'B':3.0, 'C+':2.5, 'C':2.0, 'D+':1.5, 'D':1.0, 'F':0.0, 'P':0}
    if grade in grades:    
        return grades.get(grade.upper())
    else:
        print('Invalid')

grades = ('A+', 'A', 'B+', 'B', 'C+', 'C', 'P')
total = 0
num_classes = 0
P_list = []
for grade in grades:
    if grade != 'P':
        num_classes += 1
        total += get_grade(grade)
    elif grade == 'P':
        num_classes += 1
        P_list.append('P')
    else:
        print("Invalid")

print(f"Your GPA is: {total/(num_classes - len(P_list))}")