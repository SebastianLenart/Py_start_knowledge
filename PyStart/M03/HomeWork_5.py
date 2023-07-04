def find_divisors(a):
    return {d for d in range(2, a + 1) if a % d == 0} # musi byc krotka


def find_geatest_divisor(a, b):
    div_a = find_divisors(a)
    div_b = find_divisors(b)
    return max(div_a & div_b)


print(find_geatest_divisor(9, 21)) # 3
