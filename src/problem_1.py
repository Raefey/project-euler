a = []


def sum_of_multiples_of_3_and_5(n):
    for i in range(n):
        if divisible_by_3_or_5(i):
            a.append(i)
    return sum(a)


def divisible_by_3_or_5(number):
    return number % 5 == 0 or number % 3 == 0
