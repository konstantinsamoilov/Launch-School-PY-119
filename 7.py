# This one is interesting. I thought about the integers in ASCII, and if it is possible to build some intra-comparison between the numbers within the program.
# LSBot hinted me that, since the integers are in order, subtracting ord('0') from each number in the parameter will get you the integer of each string number.
# I got to here, a list of the integers we need, but couldn't figure out a way to combine them:

def string_to_integer(string_num):
    ord_num_list = []
    result_list = []

    for el in string_num:
        ord_num_list.append(ord(el))

    for el in ord_num_list:
        result_list.append((el) - ord('0'))
        
    print(result_list)

# LSBot hint version then gave a shorter solution of this kind.
# "For each character, we update value by multiplying the existing value by 10
# (which effectively shifts the existing digits one place to the left) and then adding the new digit."

def string_to_integer(string_num):
    value = 0

    for char in string_num:
        digit = ord(char) - ord('0')
        value = (10 * value) + digit
    return value

print(string_to_integer("4321") == 4321) # value: 4, 43, 432, 4321