grade = int(input("Score of student: ".strip()))

if grade >= 80 and grade <= 100:
  print("Grade is A")
elif grade >= 50 and grade <= 79:
  print("Grade is B. Must pull up their sock's")
else:
  print("The Grade is C or D and thus the student isn't serious at all")