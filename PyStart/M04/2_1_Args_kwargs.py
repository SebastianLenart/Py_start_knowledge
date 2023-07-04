print("a", "b", sep=",")
print("-"*20)

"""
kwargs - key word arguments
args - jako tuple czyli krotka

"""


def average_args(*args): # pare argumentów naraz
    print(args)
    return sum(args)/len(args)

def save(filename, **kwargs): # jako slownikdostaniemy, do kwargs sa podwojne argumenty przekazywane
    print(filename)
    print(kwargs)

print(average_args(10, 20, 30))
print("-"*20)
save("students.txt", firstName="Seba", lastName="Lenart")
















