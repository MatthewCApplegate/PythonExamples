import random

while True:

    GuessedNumber =0
    Number = random.randint(1, 10)

    while (GuessedNumber!=Number):    
    
        GuessedNumber=input("Guess a Number! ")
            
        if (GuessedNumber==Number):
            print("Well Done!")

        elif (GuessedNumber>0 and GuessedNumber>Number):
            print("Incorrect Try A Lower Number")

        elif (GuessedNumber>0 and GuessedNumber<Number):
            print("Incorrect Try A Higher Number")
