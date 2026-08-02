try:
    x = int(input("Enter a number: "))
    print(f"x is :{x}")
# if  we enter a string instead of a number, it will raise a ValueError
except ValueError:
    print("Invalid input. Please enter a valid number.")
