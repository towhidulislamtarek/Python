from random import randint


GuessNumber = int ( input("Enter this your gase number: "))
randintNumber= randint(1,5)

if GuessNumber == randintNumber:
    print ("You have right")

else:
    print ("You have ronge")

print("This is RandintNumber is:",randintNumber)

