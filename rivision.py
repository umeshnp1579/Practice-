#                         Armstrong number

# n =int(input("Enter teh no. :"))
# c =0
# p =n
# q =n
# s =0
# while n!=0:
#     n = n//10
#     c =c+1
# while p !=0:
#     r =p%10
#     s =s+r**c
#     p = p//10
#
# if s==q:
#     print("the no. is armstring")
# else:
#     print("the no. is not armstring")

#                                 Average of number
# def average(a,b,c,d,e):
#     ans = (a+b+c+d+e)//5
#     print("The average of sum is : ",ans)
# average(1,5,45,12,7)

#                           biggest number between 3 ad 2 number
#               for three number by function
# def maxnum(a,b,c):
#     if a>b and a>c:
#         return a
#     elif b>a and b>c:
#         return b
#     else:
#         return c
# n1 =int(input("Enter the 1st no. :"))
# n2 =int(input("Enter the 2nd no. :"))
# n3 =int(input("Enter the 3rd no. :"))
# ans = maxnum(n1,n2,n3)
# print(f"The maximum number is {ans}")

#       for two number
# a =int(input("Enter rhe 1st no. :"))
# b =int(input("Enter the 2nd no. :"))
# if a>b:
#     print(f"the {a}is greter than{b}")
# else:
#     print(f"the {b}is greter than{a}")

#                       check leap year
# y =int(input("Enter a year : "))
# if y%4 ==0 and y%100!=0 or y%400==0:
#     print("THe year is leap year")
# else:
#     print("THe year is not leap year")

#                   check no. is positive or negative
# n =int(input("Enter the number :"))
# if n>0 :
#     print(f"{n} is positive")
# else:
#     print(f"{n} is Negative")

#               circle of area
# r = int(input("enter a readiase of circle"))
# area_of_circle= 22//7*(r**2)
# print(f"The area of circle is : {area_of_circle}")

#               compound iterest
# # formula ci = p(1+r/100)^t
# p =int(input("Enter the amount : "))
# r =int(input("Enter the rate : "))
# t =int(input("Enter the time : "))
# ci = p*(1+r/100)**t
# print(f"compound interest is : {ci}")

#                        countiong digit
# n =int(input("Enter tht number. :"))
# c = 0
# while n!= 0:
#     n = n//10
#     c = c+1
# print(f"the digit in this number is {c}")

# #               check the number is even or odd
# n =int(input("Enter tht number. :"))
# if n%2==0:
#     print("The number is even")
# else:
#     print("The number is odd")

#  factorial
# n =int(input("Enter tht number. :"))
# f = 1
# while n!=0:
#     f =f*n
#     n = n-1
# print("the factorial is ",f)

# # solve 1+2/2!+3+3!+........+n/n!
# n =int(input("Enter tht number. :"))
# s = 0
# f = 1
# for i in range(1,n+1):
#     f = f*i
#     s = s + i/f
# print(s)

# Febonacci number
# n = int(input("Enter the number : "))
# if n==1:
#     f1 = 0
#     print(f1,end=" ")
# elif n==2:
#     f1 = 0
#     f2 = 1
#     print(f1,f2,end=" ")
# else:
#     f1 = 0
#     f2 = 1
#     print(f1,f2,end=" ")
# for i in range(2,n):
#     f3 = f1 + f2
#     f1 = f2
#     f2 = f3
#     print(f3,end=" ")

# #       check number is fibonacci or not                            5
# n = int(input("Enter the number : "))
# f1 = 0
# f2 = 1
# f3 = f1+f2
# if n==1 or n == 1:
#     print("The number is febonacci number")
# else:
#
#     while f3<n:
#         f1 = f2
#         f2 = f3
#         f3 = f1+f2
# if f3==n:
#     print("The number is febonacci number")
# else:
#     print("The number is not febonacci number")

#           gcd
# a = int(input("Enter the 1st number : "))
# b = int(input("Enter the 2nd number : "))
# for i in range(1,a+1):
#     if a%i==0 and b%i==0:
#         gcd = i
# print("The gcd is ", gcd)
#
# #  lcm
# a = int (input("Enter the 1st number"))
# b = int (input("Enter the 2nd number"))
# for i in range(1,a+1):
#     if a%i==0 and b%i==0:
#         gcd = i
# lcm  = a*b/gcd
# print(f"The lcm is{lcm}")

# Simple interest
"""
si = prt/100
"""
# #  lcm
# p = int (input("Enter the amount : "))
# r = int (input("Enter the rate : "))
# t = int (input("Enter the time : "))
# si = (p*r*t)/100
# print(f"The simple interest is {si}")

#               solve sum problem
# add two number

# a = int (input("Enter the 1st number"))
# b = int (input("Enter the 2nd number"))
# c =a+b
# print(c)
# #
# # gactorial by 3 step
# def factotial(number):
#     if number==0 or number==1:
#         return 1
#     else:
#         return number*factotial(number-1)
# n = int(input("please enter the number :"))
# print(f"The factorial of number is : {factotial(n)} ")
#
#
# # or
#
# a = int(input("enter the number: "))
# f = 1
# while a!=0:
#     f = f*a
#     a -= 1
#
# print("The factorial of number is ", f)

# # sum of digit
# n = int(input("enter the number  : "))
# s = 0
# while n !=0:
#     r = n%10
#     s = s+r
#     n = n//10
# print("The sum of digit is : ",s)

#                               palindrom 121 == 121 ,122 != 221
# n = int(input("Enter the number : "))
# p =n
# s = 0
# while n !=0:
#     r = n%10
#     s = s*10+r
#     n = n//10
# if s==p:
#     print(f"the {p} is palindrom")
# else:
#     print(f"the {p} is not palindrom")

# check number is prime or not
# n = int(input("Enter the number : "))
# c =0
# for i in range(1,n):
#     if n%i==0:
#         c = c+1
# if c==1:
#     print(f"The {n} is prime number.")
# else:
#     print(f"The {n} is not prime number.")

# print prime number between 100
# print("The prime number are : ")
# a = []
# for i in range(1,100):
#     c = 0
#     for j in range (1,i):
#         if i%j==0:
#             c = c+1
#
#     if c==1:
#         # a.append(i)
#         print(a)
#         # break

#     1+2+3+..........+n
# n = int(input("Enter the number : "))
# s = 0
# for i in range(1,n+1):
#     s = s+i
# print(s)

#                  1+2^2+3^3+..........n^n
# n = int(input("Enter the number : "))
# s = 0
# for i in range(1,n+1):
#     s = s+i**i
# print(s)

#           1^2/1+2^2/2+3^2/3+...........+n^n/n or 1+2+3+.........+n
n = int(input("Enter the number : "))
s = 0
for i in range(1,n+1):
    s = s+(i**2)//i
print(s)