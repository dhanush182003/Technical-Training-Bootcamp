num1=int(input("enter first number :"))
num2=int(input("enter second number :"))
while(num1!=num2):
    if(num1>num2):
        num1=num1-num2
    if(num2>num1):
        num2=num2-num1
print("GCD of two number is :",num1)