def get_greatest_common_divisor(a, b):  ##最大公约数
    if a == b:
        return a
    if (a & 1) == 0 and (b & 1) == 0:
        return get_greatest_common_divisor(a >> 1, b >> 1) << 1
    elif (a & 1) == 0 and (b & 1) != 0:
        return get_greatest_common_divisor(a >> 1, b)
    elif (a & 1) != 0 and (b & 1) == 0:
        return get_greatest_common_divisor(a, b >> 1)
    else:
        big = max(a, b)
        small = min(a, b)
        return get_greatest_common_divisor(big - small, small)


def lowest_common_multiple(a, b):  # 最小公倍数
    return a * b // get_greatest_common_divisor(a, b)


def permutations(m, n):  # 组合，计算A（m n）,n是总数，m是待选数
    assert m <= n
    import math
    return math.factorial(n) // (math.factorial(n - m))


def combinations(m, n):  # 排列，计算C（m n）,n是总数，m是待选数
    assert m <= n
    import math
    return math.factorial(n) // (math.factorial(m) * math.factorial(n - m))


import cProfile

cProfile.run("print(permutations(3,3))")
