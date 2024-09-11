category = {'A+':4.5, 'A':4.0, 'B+':3.5, 'B':3.0, 'C+':2.5, 'C':2.0, 'D+':1.5, 'D':1.0, 'F':0.0, 'P':0.0}
num_courses = 0
total = 0
done = False
while not done:
    grade = input()
    if grade == 'P':
        done = True
    elif grade not in category:
        pass
    else:
        num_courses += 1
        total += category[grade]
        
if num_courses > 0:
    print(f'Your GPA is: {total/num_courses:.3}')
