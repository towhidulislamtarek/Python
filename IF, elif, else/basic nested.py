num1 = int (input("Enter this 1st number: "))
num2 = int (input("Enter this 2nd number: "))
num3 = int (input("Enter this 3rd number: "))

if num1>num2:
    if num2>num3:
        print("leargest number is:",num1)

if num1<num2:
    if num2>num3:
        print("The leargest number is:",num2 )

if num1<num2:
    if num2<num3:
        print ("The leargest number: ",num3)