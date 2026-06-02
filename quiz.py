print("Greetings! This is a quiz to test your General knowledge. Don't worry if you don't know the answer to a question, just give it your best guess and then check the answer by running the code.")

# This is the introduction to the quiz.

Number_1 =input("What is the capital of France? ")
if Number_1.lower() == "paris":    
    print("Correct! The capital of France is Paris.")
else:
    print("Incorrect! The capital of France is Paris.")

#First question is asking what the capital of France is and if the user inputs "paris", it will print "Correct! The capital of France is Paris."

Number_2 = input("What is the largest planet in our solar system? ")
if Number_2.lower() == "jupiter":
    print("Correct! The largest planet in our solar system is Jupiter.")
else:
    print("incorrect! The largest planet in our soular system")
#Second question is asking what the largest planet in the solar system is and if the user input jupiter, it will print "Correct the largest planet in our solar system is Jupiter"

Number_3 = input("What is the fastest land animal? ")
if Number_3.lower() == "cheetah":
    print("Correct! The fastest land animal is the Cheetah.")
else:    
    print("Incorrect! The fastest land animal is the Cheetah.")
#Third question is asking what the fastest land animal is, if the user inputs "cheetah", its going to print "Correct! The fastest land animal is the Cheetah."

Number_4 = input("What is the smallest country in the world? ")
if Number_4.lower() == "vatican city":
    print("Correct! The smallest country in the world is Vatican City.")
else:
    print("Incorrect! The smallest country in the world is Vatican City.")
#Fourth question is asking what the smallest country in the world is. If the user inputs "vatican city", it will print "correct! The Smallest country in the world is vatican city"

true_or_false = input("True or False: The Great Wall of China is visible from space. ")
if true_or_false.lower() == "false":
    print("Correct! The Great Wall of China is not visible from space.")
else:
    print("Incorrect! The Great Wall of China is not visible from space.")
#Fifth question is asking weather the statement"The Great Wall Of China i visable from space" is true or false. If the user inputs false it will print "Correct! The Great Wall Of China is not visable from space"

if all([Number_1.lower() == "paris", Number_2.lower() == "jupiter", Number_3.lower() == "cheetah", Number_4.lower() == "vatican city", true_or_false.lower() == "false"]):
    print("Congratulations! You got all the answers correct!")
else: 
    print("Don't worry, you can always try again to get all the answers correct!")
# This code is checking if all the answers the user inputted are correct. If they are, It prints "Congratulations! You got all the answers correct!"