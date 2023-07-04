from collections.abc import Callable

# Callable[[argument_type], return_type]

def do_something(data: list, f: Callable[[list], int]):
    return f(data)

print(do_something([1,2,3], sum)) # 6
print(do_something([4,5,6], len)) # 3
print("---------")

#---------------------------------------------------------------------

def total_salary(base, calculate_extra):
    return base + calculate_extra(base)

def calculate_ten_percent(amount):
    return 0.1 * amount

print(total_salary(1000, calculate_ten_percent)) # bez nawiasów !!!

 
#---------------------------------------------------------------------