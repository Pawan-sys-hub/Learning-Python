print("Challange 1")

numbers = [12,23,43,123,1212,121]

print(numbers.append(34))
largest = max(numbers)
print(f"The largest number is - {largest}")
smallest = min(numbers)
print(f"The smallest number is {smallest}")

add = sum(numbers)
print(f"the sum of number is -- {add}")

average = add / 6 
print(f"average of the sum of number is -- {average}")

number = 2
if number / 2:
  print("even number")
else:
  print("odd")

even = [ n for n in numbers if n % 2 == 0]
print(even)

odd = [ o for o in numbers if o % 3 == 0]
print(odd)


print("Challange 2")

marks = [45,54,64,98,90,12,56]

total_marks = sum(marks)
print(f"The sum of number is {total_marks}")
average = total_marks / 2
print(f"the average marks obtain by the student is {average}")

highest_marks = max(marks)
print(f"the highest marks obtain my student is {highest_marks}")

lowest_marks = min(marks)
print(f"the lowest marks obtain by the student is {lowest_marks}")

print("using loops")

total = 0
highest_mark = marks[0]
lowest_mark = marks [0]
above_80 = 0

for m in marks:
  total += m
  if m > highest_mark:
    highest_mark = m
  if m < lowest_mark:
    lowest_mark = m
  if m > 80:
    above_80 += 1
averages = total / len(marks)
print (f"Average {averages}")
print(f"highest number {highest_mark}")
print(f"lowest nmber is {lowest_mark}")
print(f"Marks above 80 is {above_80}")