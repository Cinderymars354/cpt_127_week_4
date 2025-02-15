
#copied from assignment_2.py

with open('student_grades.csv','r') as f:

    # collect all lines from the file
    lines = f.readlines()


    # validate file has data
    if len(lines) > 0:
        grades = []

        # iterate through each line and collect the grade
        # skipping the first 'header' line
        for line in lines[1:]:
            # split the line into a list (i.e. columns)
            row = line.split(',')

            # convert the grade to a float and add it to the list
            grades.append(float(row[3].replace('\n','')))

        avg = sum(grades) / len(grades)
#to get the difference values in a list
a = 0   
difference = []     

for f in grades:
 difference.append(grades[a] - avg)
 a += 1
b = 0
c = 2

#to put the difference values in the copied file lines
for f in difference:
 lines.insert(c, difference[b])
 b += 1
 c += 2
print(lines)

#to make a new file with the differences, unfortunately two lines under instead of in the row they belong.
#I have no idea how to fix that.
with open('student_grades_difference.csv','w') as file:
   for item in lines:
    file.write(f'{item}\n')
   
   print(file)
# positive numbers = amount above avg, negatives means how far under avg, and 0 means its = with avg.