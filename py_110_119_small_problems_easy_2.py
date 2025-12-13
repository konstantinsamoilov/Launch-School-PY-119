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

# Further exploration (ongoing...):

DEGREE = "\u00B0"
CIRCLE = 360

def dms(flt):
    degrees = str(flt)
    
    if flt < -360:
        # ...
    
    if -360 < flt < 0:
        return f"{CIRCLE + flt}{DEGREE}00'00\""
    
    elif flt > 360:
        return f"{flt - CIRCLE}{DEGREE}00'00\""
    
    elif '.' not in degrees:
        return f"{degrees}{DEGREE}00'00\""
    
    else:
        split_degrees = degrees.split(".") #
        degree_bits = "." + split_degrees[1]
        minutes = float(degree_bits) * 60
        
        split_time = str(minutes).split(".")
        seconds_string = "." + split_time[1]
        seconds = float(seconds_string) * 60
        
        return f"{split_degrees[0]}{DEGREE}{int(minutes):02}'{int(seconds):02}\""

# 2:

def union(lst1, lst2):
    lst3 = lst1 + lst2
    union_set = set(lst3)
    return union_set

# 3 (what a hoot compared to the official solution):

def halvsies(lst):
    result_lst = [[], []]
    
    if len(lst) == 0:
        pass
    
    elif len(lst) == 1:
        result_lst[0] = lst
        
    elif len(lst) % 2 == 0:
        half_count = len(lst) // 2
        result_lst[0] = lst[:half_count]
        result_lst[1] = lst[half_count:]
    
    elif len(lst) % 2 != 0:
        half_count = len(lst) // 2 + 1
        result_lst[0] = lst[:half_count]
        result_lst[1] = lst[half_count:]
        
    return result_lst

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