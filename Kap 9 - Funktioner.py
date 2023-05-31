import math


# Uppgift 1
def kvadrat(val):
    return val ** 2


# Uppgift 2
def linje(amount):
    print("_" * amount)


# Uppgift 3
def maximum(v1, v2):
    if v1 > v2:
        return v1
    else:
        return v2


# Uppgift 4
def max_three(n1, n2, n3):
    m = maximum(maximum(n1, n2), n3)
    return m


# Uppgift 5
def nettopris(bruttobelopp):
    if bruttobelopp < 500:
        return bruttobelopp
    elif 500 <= bruttobelopp < 1000:
        return bruttobelopp - bruttobelopp * 0.02
    else:
        return bruttobelopp - bruttobelopp * 0.05


# Uppgift 6
def uppg6(tal1: int, tal2: int, operator: str):

    match operator:
        case '+':
            return tal1 + tal2
        case '-':
            return tal1 - tal2
        case '*':
            return tal1 * tal2
        case '/':
            return tal1 / tal2
        case _:
            print("Values do not match expected")


def uppg7():
    area = float(input("Input area of circle: "))
    r = math.sqrt(area / math.pi)
    print("The radius has a value of ", r, "unit(s) of length")


def uppg8(n):
    # Uppgift a
    fib = [1, 1]
    fib_quo = []
    for i in range(n - 2):
        fib.append(fib[i] + fib[i + 1])
        # Uppgift b
        fib_quo.append(fib[i + 2] / fib[i + 1])
    print(fib)
    print(fib_quo)
    # Uppgift c
    print((1 + math.sqrt(5)) / 2)


def fibonacci(n):
    n1 = 1
    n2 = 1
    for _ in range(n - 2):
        temp = n1 + n2
        n1 = n2
        n2 = temp
    return n2


# Main
def main():
    """print(kvadrat(2))
    linje(4)
    print(maximum(24, 5))
    print(max_three(8, 2, 3))
    print(nettopris(1000))
    print(uppg6(2, 3, "-"))
    uppg7()
    uppg8(10)
    print(fibonacci(10))"""


main()
