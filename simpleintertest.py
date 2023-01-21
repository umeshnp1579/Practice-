# Simole interest count using by python
"""
the formula of simple interest is
        si = ptr/100 ; where
        si = simple interest
        p = amount
        r = interest rate
        t = time

        input :
        p =3000
        t = 1
        r = 7
        output  : 210
        we run as practical
"""
p = int(input("Enter the amount : "))
r = int(input("Enter the interest rate : "))
t = int(input("Enter the time : "))
si = (p*t*r)/100
print(f"The Simple inmterest of givan amount is {si}")