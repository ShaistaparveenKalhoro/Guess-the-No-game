import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # could also be high since low = high
            
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)? ').lower()
        
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
            
    print(f'Yay! The computer guessed your number, {guess}, correctly!')

print("Welcome to the Number Guessing Game!")
print("Think of a number between 1 and 100.")
print("I'll try to guess it!")

computer_guess(100) 