print("WELCOME TO ATM BANKING SYSTEM")
print("Enter Your Card")

#one method using if else loops 
PIN_Number = int(input("Enter the PIN Number of your ATM : "))
if PIN_Number == 1234:
  print("Welcome")
else:
  print("Wrong PIN Number")

#another method using while loop 

PIN_Number = input("Enter the PIN_NUMBER")
while PIN_Number =="1234":
  name = input("Enter the number:")
  print("Please enter the number:")