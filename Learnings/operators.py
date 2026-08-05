print ("arithmetric operators")

a = int(input("Enter the first number ="))
b = int(input("Enter the second number ="))
print(a + b)
print(a * b)
print(a - b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
print("Comparison")
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a <= b)
print(a >= b)
print("Logical")
print(a > 0 and a < 12)
print(a > 0 or a < 14)
print(not(a > 0 and a < 500))


print("check your age are you Adult or Younger")

age = int(input("Enter your sweet age that is you dont want to share is :"))
if age >= 18:
  print("you are adult as i am")
else:
  print("You are too small")


print(" lets check your marks")
Marks = int(input("Enter your marks here :"))

if Marks >= 90:
  print("congrats BRo for A+")
elif Marks >= 80:
  print("You score A")
elif Marks >= 70:
  print("b+ hahahahhahah")
else:
  print("fail")


  print ("lets doo LOOPS")

for i in range (1 ,11):
  print (i)

  for pawan in range (1,3):
    print(pawan)

