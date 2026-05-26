#find the given number is odd or given 
print("EVEN OR ODD")

Number = int(input("Enter the number:"))

if Number % 2 == 0:
  print("Even")
else:
  print("odd")


#quiz

print("Lets play game ")

quection = input("Who is going to win 2026 worldcup?")

answer = ("nepal")

if quection.lower() == answer:
  print("correct")
else:
  print("2026worldcup = PORTUGAL")


  #multiplication table 

  print("MUltipLication")

  multiply = int(input("ENter a number you want to have multiplication table "))
  
  for i in range (1, 11):
    print(f"{multiply} * {1} = {multiply * i}")



    #multiplication number
    print("lets create multiply table ")

    number = int(input("enter the number for multiplication"))

    for j in range (1, 11):

      print(f"{number} * {j} = {number * j}")