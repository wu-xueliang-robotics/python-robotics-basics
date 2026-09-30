import random

target = random.randint(1,99)
count = 0

def give_hint(guess,target):
    if guess > target:
        return "you guess is large"
    elif guess < target:
        return "you guess is small"
    else:
        return "you are right"

while True:
    user_input = int(input("please input the number of you guess:"))
    if user_input == 0:
        break
    count = count + 1
    result = give_hint(user_input,target)
    print(result)
    if result == "you are right":
        print(f"Good!you guess right,total is {count}")
        break