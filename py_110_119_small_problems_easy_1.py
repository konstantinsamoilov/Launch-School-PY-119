# Easy 1

# 1

num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))
num3 = float(input("Enter the 3rd number: "))
num4 = float(input("Enter the 4th number: "))
num5 = float(input("Enter the 5th number: "))
num6 = float(input("Enter the last number: "))

if num6 in [num1, num2, num3, num4, num5]:
    print(f"{num6} is in {num1, num2, num3, num4, num5}.")
else:
    print(f"{num6} isn't in {num1, num2, num3, num4, num5}.")
# The number collection is in a tuple instead of exactly like the solution is.

# Further exploration:
# LSBot described it as: instead of checking whether the 6th input matches any of the first five numbers, 
# check whether any of the first five numbers meet some condition (here it's greater than 25).

num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))
num3 = float(input("Enter the 3rd number: "))
num4 = float(input("Enter the 4th number: "))
num5 = float(input("Enter the 5th number: "))

greater_than = any(num > 25 for num in [num1, num2, num3, num4, num5])

if greater_than:
    print("Yes!")
else:
    print("No!")

# 2

