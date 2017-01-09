import random

while True:
    
    print("You choose a Number between 1 and 100.")
    MinNumber=1
    MaxNumber=100
    QUESTION="NO"
    
    while (QUESTION!="YES"):
        GuessedNumber = random.randint(MinNumber, MaxNumber)

        QUESTION=raw_input ("Is it "+str(GuessedNumber)+"? YES,HIGHER OR LOWER? ")
    
        if (QUESTION=="YES"):
            print("HOORAY!")

        elif (QUESTION=="HIGHER"):
            print("OK I'll try a higher number")
            MinNumber=GuessedNumber+1

        elif (QUESTION=="LOWER"):
            print("OK I'll try a lower number")
            MaxNumber=GuessedNumber-1
