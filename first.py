#MY first genuine python program, made a bug already

name = input("What is your name? ")

#removing whitespaces from both age and name variable 

name = name.strip()
age = input("What is your age? ")

age =  age.strip()
print(f"Hello {name} who is {age} years old")

print("it should work perfecto")