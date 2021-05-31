# Выписав первые шесть простых чисел, получим 2, 3, 5, 7, 11 и 13.
# Очевидно, что 6-е простое число - 13.
#
# Какое число является 10001-м простым числом?

def prime(n):
    prime_list = [2]
    num = 3
    while n > len(prime_list):
        count = 0
        for i in prime_list:
            if num % i == 0:
                count += 1
        if count == 0:
            prime_list.append(num)
        num += 2
    return prime_list[-1]


print(prime(10001))

# Answer - 104743
