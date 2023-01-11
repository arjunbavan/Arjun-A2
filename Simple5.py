print("1.ADDITION")
print("2.SUBTRACTION")
print("3.MULTIPICATION")
print("4.DIVISION")
calc=int(input("Enter the opperation: "))
a=int(input("enter the a number: "))
b=int(input("enter the b number: "))
if(calc==1):
    print("Add: ",a+b)
elif(calc==2):
    print("Sub: ",a-b)
elif(calc==3):
    print("mul: ",a*b)
elif(calc==4):
    print("div: ",a/b)
