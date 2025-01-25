# father1.py
name = "joe"
sons = 2
daughters = 3

# ----- ENTER YOUR CODE HERE --------


s = f"{name.capitalize()} has {sons+daughters} kids."

# -----------------------------------
assert s == "Joe has 5 kids."
print("OK")

father = input("What is the name of the father?")
fatherSons = input("How many sons does he have?")
fatherDaughters = input("How many daughters does he have?")

fatherInfo = f"{father} has {fatherSons+fatherDaughters} kids.".capitalize()
print(fatherInfo)
