# the program that askes questions
# and you answer them
# at last you get your score

questions = ("How many planets solar system has?  ",
             "Which part doesnt needs to have in motherboard? ",
             "Which book is writen by Dostoyevski? ",
             "Which one is the fastest? ")

options = (("A. 6 ","B. 7 ","C. 8 ","D. 9 "),
           ("A. GPU ","B. CPU ","C. RAM ","D. Power Supply "),
           ("A. Crime and Punishment ","B. Martin Eden ","C. 1984 ","D. Animal Farm "),
           ("A. C ","B. C++ ","C. Python ","D. Assembly "))

answers = ("C","D","A","D")
guesses = []
question_num = 0
score = 0
print(" ")

for question in questions:
    print(question)
    print()
    for option in options[question_num]:
        print(option, end=" ")
        print()

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"The correct answer is {answers[question_num]}")
    question_num += 1

total = (score/len(questions))* 100
print(f"Your score is {total}%")
