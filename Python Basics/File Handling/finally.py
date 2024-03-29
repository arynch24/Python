try:
    x = int(input("Enter a number: "))
    result = 10 / x
except ValueError:
    print("Invalid input. Please enter a valid number.")
except ZeroDivisionError:
    print("You cannot divide by zero.")
else:
    print("The result is:", result)
finally:
    print("Execution finished.")