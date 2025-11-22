numOfWords = 0
numOfLetters = 0
numOfDigits = 0

text = input ("Enter a text of number: ")

for x in text:
    x = x.lower()
    if x>='a' and x<='z':
        numOfLetters = numOfLetters+1
        
        
    elif x>='0' and x<='9':
        numOfDigits= numOfDigits+1


    elif x ==' ':
        numOfWords = numOfWords+1


print ("The number of letter: ",numOfLetters)
print ("The number of digits : ",numOfDigits)
print ("The number of word",numOfWords)
