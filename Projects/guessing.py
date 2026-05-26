#lets guess the number until you find 


print("Welcome to guess game")
print("Are you READY!")
print("Lets GOO")

guess = int(input("Enter The Number:"))
number = 512

for i in range(1,500):
 print(f"{guess}= {guess <= i} TOO low")
 print(f"{guess} = {guess >i} Too high")



if guess == number:
  print("You guess right")

else:
  print("Try again")