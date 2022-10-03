import random
print("Welcome to my Casino")

random_number = random.randint(-1,101)
print(random_number)

question_one = int(input("What do you think the number will be the number is between 0 and 100: "))

if random_number == question_one:
    print("WOW nice you got it right well done...")
else:
        print("Ohhh you got it wrong try your luck next time")

input("Press any Key to Close...")        



