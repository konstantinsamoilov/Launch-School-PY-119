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

def is_palindrome(string):
    if string == string[::-1]:
        return True
    return False

# 3

def is_real_palindrome(string):
    alnum_lower = ''
    
    for char in string:
        if char.isalnum():
            alnum_lower += char
            
    return alnum_lower.casefold() == alnum_lower.casefold()[::-1]

# 4

def running_total(lst):
    result = []
    summed = 0
    
    for num in lst:
        summed += num
        result.append(summed)
        
    return result