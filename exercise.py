# Making calculator using python
a = int(input("Enter a value of a : "))
operator = input("Enter operator (+,-,*,/,%,//) : ")
b = int(input("Enter a value of b : "))

if operator == "+" :
    print(a+b)
elif operator == "-" :
    print(a-b)
elif operator == "*" :
    print(a*b)
elif operator == "/" :
    print(a/b)
elif operator == "//" :
    print(a//b)
elif operator == "%" :
    print(a%b)
else:
    print("Enter selected operator")

#  print star pattern

n = int(input("How many rows and colounm you want : "))
bool_var = int(input("Please select 1 or 0 1 is for starting and 0 is for inverse star patern : "))
if bool_var==1:
    for i in range(0,n+1):
        for j in range(i):
            print("*",end=" ")
        print()
if bool_var == 0:
    for i in range(n,0,-1):
        for j in range(i):
            print("*", end=" ")
        print()
