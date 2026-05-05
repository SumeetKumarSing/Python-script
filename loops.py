for i in range(5):
    print(i)

"""
Output is
0
1
2
3
4
"""
#-------------------------
for x in range(2, 8, 2):
    print(x)

"""
Output is
2
4
6
"""
#-------------------------
a = 0

while a < 5:
    print(a)
    a += 1

"""Output is
0
1
2
3
4
"""

# This is a simple program to determine the grade of a student based on their marks using both for loop and while loop.
for i in range(5):
    a = int(input("Type the marks: "))
    if a >= 90:
        print("You obtain A grade")
    elif a >= 80:
        print("You obtain B grade")

    elif a >= 60:
        print("You obtain C grade")
    else:
        print("FAIL")

# ========================

x = 0

while x < 5:
    a = int(input("Type the marks: "))
    if a >= 90:
        print("You obtain A grade")
        x += 1
    elif a >= 80:
        print("You obtain B grade")
        x += 1
    elif a >= 60:
        print("You obtain C grade")
        x += 1
    else:
        print("FAIL")
        x += 1

#=======================
# Control statements in loops
for a in range(1,6):
    if a == 4:
        break
    print(a)

"""
Output is
1
2
3

"""
#=================
for i in range(1,6):
    if i == 4:
        continue
    print(i)
"""
Output is
1
2
3
5
"""