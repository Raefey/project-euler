a = []

def sum_of_multiples_of_3_and_5(n):
    for i in range(n):
        a.append(i + 1)
    return sum(a)