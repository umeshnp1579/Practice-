# frbonacci no.are 1,1,2,3,5,8,13
# 1,1+0,1+1,2+1,3+2,5+3,8+5,...............
n = int(input("Enter the no. for febonacci : "))
if n==1:
    f1 = 0
    print(f1)
elif n==2:
    f1 =0
    f2 =1
    print(f1,f2,end=" ")
else:
    f1 = 0
    f2 = 1
    print(f1,f2,end=" ")
for i in range(2,n):
    f3 = f1+f2
    f1 = f2
    f2 = f3
    print(f3, end=" ")

