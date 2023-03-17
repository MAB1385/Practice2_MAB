"""
The sum of the digits of the number
"""

#! To sum of the digits of the number 
def sum_digits(number= int) -> int:
    digits_list= [int(i) for i in str(number)]
    return sum(digits_list)

#--------------------------------------------------------------------------------------
#========================================test==========================================
number= int(input('Enter number = '))
print(sum_digits(number))