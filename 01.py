"""
formula(n) ---->  (1+2/3)*(2+2/3)*...*(n+2/3)
"""
#! To apply the formula 
def fun(n= int) -> int:
    return n + 2/3


def fact(number= int) -> int:
    temp= 1
    for i in range(1,number):
        temp*= fun(i)
    return temp

#--------------------------------------------------------------------------------------
#========================================test==========================================
print(fact(2))