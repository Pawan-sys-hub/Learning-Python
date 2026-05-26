#student marks calculator 

print("Student of Kathmandu Model College")

print("BCA Result 2023 Batch of 5th Semister")

marks = float(input("Enter the total marks you got : "))

percentage = marks / 800 * 100

print("Total Percentage you got :", percentage)



if percentage >=90:

  print("You got A+")

elif percentage >=80:
  print("You got A")

elif percentage >=70:
  print("you got B+")

else:
  print("Fail go and read")