# 2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.
# Какое самое маленькое число делится нацело на все числа от 1 до 20?

def gcd(a, b):
    while b > 0 or a > 0:
        a, b = b, a % b
        if a == 0:
            return b
        if b == 0:
            return a


def lcm(a, b):
    return a * b // gcd(a, b)  # integer division


d = 1
for i in range(2, 21):  # last i=20
    d = lcm(d, i)

print(d)

# Answer - 232792560
