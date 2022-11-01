#cti 11-
#P4HW1
#Luke Rohweder
#11/1/2022

#Ask the user for 6 grades for the 6 modules.
#Add them to a list.

grades = []

for grade in range(6):
    grade = int(input("Enter grade: "))
    grades.append(grade)
                
print("The grade are: ", grades)
#max (grades) and min(grades)
#to show lowest and highest in the list
print("Highest grade is: ", max(grades))
print("Lowest grade is: ", min(grades))

total = sum(grades)
count= len(grades)
average = total/count
print("Total is: ", total)
print("Count is: ", count)
print("Average is: ", average)
    
