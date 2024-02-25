print("Welcome User!! Let's play!")

name = input("Your name? ")

playing = input("Wanna play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's Play!! " + str(name) +":D")
score = 0

answer = input("What is the powerhouse of the cell? ")
if answer.lower() == "mitochondria":
    print('Correct!^o^')
    score += 1
else:
    print("oops! wrong!>v<") 

answer = input("Who is known as the 'Father of Computer Science'? ")
if answer.lower() == "alan turing":
    print('Correct!^o^')
    score += 1
else:
    print("oops! wrong!>v<") 

answer = input("What is the largest mammal on Earth? ")
if answer.lower() == "blue whale":
    print('Correct!^o^')
    score += 1
else:
    print("oops! wrong!>v<") 

answer = input("Which planet is known as the 'Red Planet'? ")
if answer.lower() == "mars":
    print('Correct!^o^')
    score += 1
else:
    print("oops! wrong!>v<") 

answer = input("What is the chemical symbol for water? ")
if answer.lower() == "h2o":
    print('Correct!^o^')
    score += 1
else:
    print("oops! wrong!>v<") 

answer = input("Who wrote the play 'Hamlet'? ")
if answer.lower() == "william shakespeare":
    print('Correct!^o^')
    score += 1
else:
    print("oops! wrong!>v<") 

answer = input("What is the largest ocean on Earth? ")
if answer.lower() == "pacific ocean":
    print('Correct!^o^')
    score += 1
else:
    print("oops! wrong!>v<") 

answer = input("In what year did the first moon landing occur? ")
if answer == "1969":
    print('Correct!^o^')
    score += 1
else:
    print("oops! wrong!>v<") 

answer = input("What is the process by which plants make their own food? ")
if answer.lower() == "photosynthesis":
    print('Correct!^o^')
    score += 1
else:
    print("oops! wrong!>v<") 

answer = input("Who developed the theory of relativity? ")
if answer.lower() == "albert einstein":
    print('Correct!^o^')
    score += 1
else:
    print("oops! wrong!>v<") 

print("You got " + str(score) + " questions correct!")
print("You got" + str((score / 10) * 100) + "%.")