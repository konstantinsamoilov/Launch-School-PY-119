# 1, woof:

DEGREE = "\u00B0"

def dms(flt):
    degrees = str(flt)
    
    if '.' not in degrees:
        return f"{degrees}{DEGREE}00'00\""
    else:
        split_degrees = degrees.split(".") #
        degree_bits = "." + split_degrees[1]
        minutes = float(degree_bits) * 60
        
        split_time = str(minutes).split(".")
        seconds_string = "." + split_time[1]
        seconds = float(seconds_string) * 60
        
        return f"{split_degrees[0]}{DEGREE}{int(minutes):02}'{int(seconds):02}\""

# Further exploration:

# ...

# 2:

def union(lst1, lst2):
    lst3 = lst1 + lst2
    union_set = set(lst3)
    return union_set

# 3:

# ...

# 4:

def find_dup(lst):
    seen = set()

    for num in lst:
        if num in seen:
            return num
        seen.add(num)
# Or:
def find_dup(lst):
    for num in lst:
        if lst.count(num) == 2:
            return num
        
# 5: 

def interleave(list1, list2):
    result = []
    zipped = zip(list1, list2)
    zipped_list = list(zipped)
    
    for pair in zipped_list:
        for el in pair:
            result.append(el)
    return result

# There are two more simple versions, one also using zip, aside from the official solution.

# 6:

# ...