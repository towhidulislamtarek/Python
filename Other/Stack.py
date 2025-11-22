books =[]
books.append("Larn C")
books.append("Larn c++")
books.append("Java")
books.append("python")

"""
append deya book stor korta hoy. nes thka upor pojonto lakta hoba,
mana nesar lakata aga hoba upor ar laka ta nesa hoba . jamon
aga hoba python ta aga hoba , tarpor java hoba , tarpor hoba larn c++,
trpor larn c hoba, ay vava lakta hoba. mana nesarta upora ar uporta nesa hoba.
"""
print(books)

books.pop() 

"""
print (book) ay vava lakla nes thaka upor print hoba
ar jode book.pop() ay vava lakla book remove hoba
nesar ja book ta asa oyta remove hoba. jamon python remove hoba. 
"""
print(books) #ayta dela remove hobyr por ja koyta takba oy koyta print hoba.

print("Now the top book is: ",books[-1])
#ayta dela java print hoba. book.pop()ar karona python remove hoya gasa. taii java print hoba.

if not books:
    print("No books left")
    #same ayta pop ar moto kaj korba