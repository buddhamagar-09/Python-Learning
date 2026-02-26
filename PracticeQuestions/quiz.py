# creating a quiz game in python

questions = ("How many elements are there in the periodic table? ",
             "Which animal lays the largest eggs? ",
             "Which is the tallest mountain in the world? ",
             "What is the national bird of Nepal? ",
             "How many Provinces are there in Nepal"
)

options = (("A. 117","B. 120","C. 112","D. 125"),
           ("A. WWhale","B. Snake","C. Hen","D. Crocodile"),
           ("A. Mt K2","B. Mt KanchanJunga","C. Mt Kailash","D. Mt Everest"),
           ("A. Crow","B. Danphe","C. Parrot","D. Sparrow"),
           ("A. 7","B. 4","C. 8","D. 5"))

answers = ["B","A","D","B","A"]
guesses = []
score = 0
question_num = 0   

for question in questions:
    print("---------------------------------")
    print(f"{question}")
    for option in options[question_num]:
        print(option)
    guess = input("Enter the option A/B/C/D : ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        print("Correct")
        score += 1
    else:
        print("incorrect!")
        print(f"The correct option is {answers[question_num]}")
    question_num += 1

print("---------------------------")
print("----------Results----------")
print("---------------------------")

print("Guesses: ",end=" ")
for guess in guesses:
    print(guess,end=" ")
print()

print("Answers: ",end=" ")
for answer in answers:
    print(answer,end=" ")
print()

score = int(score/len(questions))*100
print(f"Your Total score is {score}")