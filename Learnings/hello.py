print("problem solving of students")
name = input("Enter your name :")
marks = []
number_of_subject = 5

#input
for i in range (number_of_subject):
  mark = float(input(f"Enter the marks for subjects {i + 1}:"))
  marks.append(mark)

#calculation 

total_marks = sum(marks)
average_marks = total_marks / number_of_subject 
percentage = total_marks / 500 * 100

#output 
print(f"sum of total marks {total_marks} " )
print(f"average marks : {average_marks}")
print(f"percentage: {percentage}")