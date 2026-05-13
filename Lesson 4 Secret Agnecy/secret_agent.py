### Secret Agent Login
# Create a login process for a secret agent
  
# Ask for the user's name and save it in a variable
name=input("What is your name? ")

# Ask for the password and save it in a variable
password=input("What is the password? ")
# Check if the password == 'Falcon'
if password == "Falcon": 
    # Output that access has been granted and welcome user using their name
    print(f"Access granted. Welcome, {name}!")

    # Ask for the user's age and save it in a variable
    age = input("What is your age? ")

    # Change the age into an integer
    age = int(age)

    # If the user's age is under 13, tell them they are a spy in training
    if age < 13:
        print("You are a spy in training.")
    # If their age is under 18, tell them they are a junior spy
    elif age < 18:
        print("You are a junior spy.")
    # If their age is 18 or over, tell them they are a Field Agent
    else:
        print("You are a Field Agent.")

# Output a goodbye

name=print("Goodbye, " + name + ".")

# ___________________________

# EXTENSION

# Ask more questions to give your spy more information
# Look up how to use 'and' and 'or' to force more conditions (eg. they must be one of 3 users AND get the password correct)

# ___________________________

# EXPERT (For those who already know python)

