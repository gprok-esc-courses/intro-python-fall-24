import random 

secret = random.randint(1, 100)
guess = 0
counter = 0

print(secret)

while(guess != secret):
    guess = int(input("Guess: "))
    counter = counter + 1
    if guess > secret:
        print("Go DOWN")
    elif guess < secret:
        print("Go UP")
    else:
        print("Found! in", counter, "guesses")