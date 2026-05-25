#creating simple calculator

print("Calculator")

Firstnumber =  int(input("Enter the first number:"))
Secondnumber = int(input("Enter the second number:"))

calculation = input("Enter the Symbol (+-*/)")


if calculation == "+":
  result = (Firstnumber + Secondnumber)
  print(" SUm of the numbers is:" ,result )

elif calculation == "-":
    result = Firstnumber - Secondnumber
    print("difference of the number is " , result)

elif calculation == "*":
  result = Firstnumber * Secondnumber
  print=("multiplication of two number:",result)

elif calculation == "/":
   result = Firstnumber / Secondnumber 
   print = ("Division of two number is :" ,result)
else:
   print("Invalid number")


