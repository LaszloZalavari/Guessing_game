from random import randint
guesslist = []
guessdiff = []
num = randint(1,100)

while True:
    guess = int(input("What is your guess?: "))
    diff = abs(guess-num)
    guesslist.append(guess)
    guessdiff.append(diff)
    
    if 1 <= guess <= 100:
        
        if guess == num:
            print("Congratulations! You have guessed correctly, the number was {} indeed and it took you {} guesses to fnd it.".format(num, len(guesslist)))
            break
        
        elif len(guesslist) == 1 and diff < 10:
            print("WARM!")
            
        elif len(guesslist) == 1 and diff > 10:
            print("COLD!")
        
        else:
            if diff < guessdiff[-2]:
                print("WARMER")
            elif diff == guessdiff[-2]:
                print("You are the same distance from the number as on your previous guess")
            else:
                print("COLDER!")
            
    else:
        print("You broke the rules. Your guess is out of bounds.")
