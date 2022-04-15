
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
