#pratice 

print("calculator")

num1 = int(input("Enter the number first:"))

num2 = int(input("Enter the number first:"))

calculate = input("Enter a sytmbol to calculayte +-*/: ")

if calculate == "+":
  result = num1 + num2 
  print ("sum of number is:" ,result)

elif calculate == "-":
  result = num1 -num2
  print ("Difference:", result)

elif calculate == "*":
  result = num1 * num2
  print ("multiplication:", result)

elif calculate == "/":
  result = num1 / num2
  print ("DiffereDivision:", result)

else:
  print("portugal will win 2026")



sum = num1 + num2

for i in range (1,11):
 print(f"{sum} * {i} = {sum * i}")
 
