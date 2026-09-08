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
