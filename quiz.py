while True:
    print("Greetings! This is a quiz to test your General knowledge. Don't worry if you don't know the answer to a question, just give it your best guess and then check the answer by running the code.")
    score = 0
# This is the introduction to the quiz.

    Number_1 =input("What is the capital of France? ")
    if Number_1.lower().strip() == "paris":    
        print("Correct! The capital of France is Paris.")
        score += 1
    else:
        print("Incorrect! The capital of France is Paris.")
#First question is asking what the capital of France is and if the user inputs "paris", it will print "Correct! The capital of France is Paris."

    Number_2 = input("What is the largest planet in our solar system? ")
    if Number_2.lower() == "jupiter":
        print("Correct! The largest planet in our solar system is Jupiter.")
        score += 1
    else:
        print("Incorrect! That is not the largest planet in our solar system.")
#Second question is asking what the largest planet in the solar system is and if the user input jupiter, it will print "Correct the largest planet in our solar system is Jupiter"

    Number_3 = input("What is the fastest land animal? ")
    if Number_3.lower().strip() == "cheetah":
        print("Correct! The fastest land animal is the Cheetah.")
        score += 1
    else:    
        print("Incorrect! The fastest land animal is the Cheetah.")
#Third question is asking what the fastest land animal is, if the user inputs "cheetah", its going to print "Correct! The fastest land animal is the Cheetah."

    Number_4 = input("What is the smallest country in the world? ")
    if Number_4.lower().strip() == "vatican city":
        print("Correct! The smallest country in the world is Vatican City.")
        score += 1
    else:
        print("Incorrect! The smallest country in the world is Vatican City.")
#Fourth question is asking what the smallest country in the world is. If the user inputs "vatican city", it will print "correct! The Smallest country in the world is vatican city"

    true_or_false = input("True or False: The Great Wall of China is visible from space. ")
    if true_or_false.lower() == "false":
        print("Correct! The Great Wall of China is not visible from space.")
        score += 1
    else:
        print("Incorrect! The Great Wall of China is not visible from space.")
#Fifth question is asking weather the statement"The Great Wall Of China i visable from space" is true or false. If the user inputs false it will print "Correct! The Great Wall Of China is not visable from space"

    if score == 5:
        print("Congratulations! You got all the answers correct!")
    elif score == 0:
        print("You Suck! You got all the answers wrong.")
    else:
        print(f"You got {score} out of 5 questions correct. Do you want to try again?")
    while True:
        try_again = input("Enter 'yes' to try again or 'no' to quit: ")
        if try_again.lower() == "yes":
            break
        elif try_again.lower() == "no":
            print("Thanks for playing!")
            exit()
        else:
            print("Please enter 'yes' or 'no'.")

# This is the final part of the code that checks the user's score and prints a message based on how many questions they got correct. If they got all 5 correct, it congratulates them. If they got none correct, it tells them they did poorly. Otherwise, it tells them how many they got correct and encourages them to try again.