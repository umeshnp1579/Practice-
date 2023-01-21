# Add two no.
a = int(input())
b = int(input())
c = a+b
print(f"sum of two no. is : {c}")

# Factorial of a number
#
# 5! = 5*4*3*2*1
n = int(input("Enter a number : "))
f = 1
a=0
while a!= n:
    f = f*n
    n = n-1
print(f"Factorian of given no. is : {f}")

#                         # or
a = int(input("Enter a nmber : "))
def fac(num):
    if num == 0 or num==1:
        return 1
    if num >1:
        return num*fac(num-1)
print("The factorial of given no. is : ",fac(a))


                    # or

def fac(n):
    f = 1
    a = 0
    if n==0 or n==1:
        return 1
    else:
        while a!=n:
            f = f*n
            n -= 1
        return f
n = int(input("Enter a value of a : "))
print(f"the factoriaal is : {fac(n)}")

# 5*4*3*2*1