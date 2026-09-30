print("WELCOME TO ATM BANKING SYSTEM")
print("Enter Your Card")

#one method using if else loops 
#PIN_Number = int(input("Enter the PIN Number of your ATM : "))
#if PIN_Number == 1234:
 # print("Welcome")
#else:
#  print("Wrong PIN Number")

#another method using while loop 

PIN_Number = input("Enter the PIN_NUMBER: ")
while not PIN_Number == "1234":
  print("Please enter the number: ")
  PIN_Number = input("Enter the number: ")
  