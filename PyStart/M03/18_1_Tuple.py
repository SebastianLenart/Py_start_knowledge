tuples = [
    (1,),
    (1, 2),
    (1, 2, 3),
    (1, 2, 3, 4),
    (1, 2, 3, 4, 5),
    (1, 2, 3, 4, 5, 6)
]

filtered = [sum(item) if len(item) % 2 == 0 else sum(item)/len(item)
            for item in tuples if 1 < len(item) < 6]
print(filtered)
