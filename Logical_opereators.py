# Logical operators used in python

a = 20
b = 10

print( a > b and a > b)

"""
Output of above is
True
And operator returns True if both the operands are true. If not, it returns False.

"""

print( a > b or a < b)
"""
output of above is
True
Or operator returns True if either of the operands is true. If not, it returns False.
"""

print( not(a > b))

"""
output of above is
False
Not operator returns False if the operand is true. If not, it returns True.
"""