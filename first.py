#create my own function

def hello(to):
      print("HI,", to)

name = input("What is your name? ").strip().title()
age = input("What is your age? ").strip()

print(f"Hello {name} who is {age} years old.\nIt should work perfecto")

hello(name)
