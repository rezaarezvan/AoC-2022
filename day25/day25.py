BASE_5 = {
    '2': 2,
    '1': 1,
    '0': 0,
    '-': -1,
    '=': -2
}

DATA = open('input').read()

sum = 0
for number in DATA.strip().split("\n"):
    N = 0
    for digit in number:
        N *= 5
        N += BASE_5[digit]

    sum += N

print(f"In base 10, the sum is {sum}")


def f(n):
    if n == 0:
        return []
    if (n % 5) == 0:
        return ["0"] + f(n // 5)
    if (n % 5) == 1:
        return ["1"] + f(n // 5)
    if (n % 5) == 2:
        return ["2"] + f(n // 5)
    if (n % 5) == 3:
        return ["="] + f((n + 2) // 5)
    if (n % 5) == 4:
        return ["-"] + f((n + 1) // 5)


answer = "".join(f(sum))[::-1]
print(f"In base 5, the sum is: {answer}")
