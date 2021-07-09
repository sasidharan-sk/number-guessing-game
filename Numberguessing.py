import random
import math
# Taking input
lower = int(input('\n enter the lowerbound : '))
# Taking input
upper = int(input('\n enter the upperbound : '))

# Generating random number between 
# lower and upper
a = random.randint(lower, upper)

# formula for making chances 
# depends upon lower and upper 
chances = round(math.log(upper-lower + 1,2))

print(f'\n you\'ve only {chances} chances to guess the number')

# initialising the number of guesses
count = 0

# For caluculation of minimum number of guesses
while count<chances:

    count+=1

    # taking guessing number as user input
    guess = int(input('\n Guess the number : '))

    # checking condition
    if a == guess:
        print(f'\n congrats you did it in {count} try ')

        # after a successful guess, loop will break
        break

    elif a>guess:
        if chances>0:
           chances-=1
           count-=1
           print('\n you\'ve guessed too small')
           print(f'\n you\'ve only {chances} chances to guess the number')

    elif a<guess:
        if chances>0:
            chances-=1
            count-=1
            print('\n you\'ve guessed too high')
            print(f'\n you\'ve only {chances} chances to guess the number')

# if user has no chances left
if chances==0:
        print(f'\n The number is : {a}')
        print('\n -- BETTER LUCK NEXT TIME --')
    
            
 
                









