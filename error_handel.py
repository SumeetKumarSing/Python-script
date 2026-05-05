try:
    x = int(input("Type the numerator value : "))
    y = int(input("Type the denominator value : "))
    print(x/y)
except ZeroDivisionError:
    print("denominator can't be 0")
except ValueError:
    print("Incorrect value type in no")
else:
    print("Every thing went well")
finally:
    print("Thanks for coming")