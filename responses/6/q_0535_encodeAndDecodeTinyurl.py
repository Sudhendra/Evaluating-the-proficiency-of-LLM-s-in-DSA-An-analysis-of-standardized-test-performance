def reverse_integer(n):
    reversed_n = 0
    is_negative = False

    if n < 0:
        is_negative = True
        n = -n

    while n != 0:
        digit = n % 10
        reversed_n = reversed_n * 10 + digit
        n //= 10

    if is_negative:
        reversed_n = -reversed_n

    return reversed_n
