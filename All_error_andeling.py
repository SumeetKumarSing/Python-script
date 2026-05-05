try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    
    result = a / b
    print("Result:", result)

except ValueError:
    print("❌ Invalid input! Please enter numbers only.")

except ZeroDivisionError:
    print("❌ Cannot divide by zero.")

except TypeError:
    print("❌ Type error occurred.")

except Exception as e:
    # catches any other unexpected errors
    print("❌ Something went wrong:", e)

else:
    print("✅ Program executed successfully.")

finally:
    print("🔚 Program finished (this always runs).")