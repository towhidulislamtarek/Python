lepe_year = int(input("Enter your year: "))

if(lepe_year%400==0):
    print("This is leep year")

elif(lepe_year%100==0):
    print("This is not leep year")

elif(lepe_year%4==0):
    print("This is leep year")

else:
    print("This is not leep year")