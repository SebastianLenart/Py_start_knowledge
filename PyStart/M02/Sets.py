divisibleBy3 = set(range(3,1001, 3))
divisibleBy5 = set(range(5,1001, 5))
print(divisibleBy3)
print(sorted(list(divisibleBy3 & divisibleBy5)))

