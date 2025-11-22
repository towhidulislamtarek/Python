num1 = int (input("Enter this 1st number: "))
num2 = int (input("Enter this 2nd number: "))
num3 = int (input("Enter this 3rd number: "))

if num1>num2 and num1>num3:
    print("The leargest number is: ",num1)

elif num1<num2 and num2>num3:
    print("The leargestr number is: ",num2)

elif num3>num1 and num3>num2:
    print("The leargest number is: ",num3)

else: 
    print("same")