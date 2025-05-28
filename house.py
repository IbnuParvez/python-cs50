name = input("Whats your name? ")

match name:
   case "Harry":
    print("Gryffindor")
   case "Draco":
    print("Slytherin")
   case _:
    print("Who are you asking about? ")