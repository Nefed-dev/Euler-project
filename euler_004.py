# Число-палиндром с обеих сторон (справа налево и слева направо)
# читается одинаково. Самое большое число-палиндром, полученное
# умножением двух двузначных чисел – 9009 = 91 × 99.
#
# Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.


def is_palindrome(num):
    raw = str(num)
    reversed_num = raw[::-1]
    if raw == reversed_num:
        return True


palindrome = []
for i in range(100, 1000):
    for j in range(100, 1000):
        if is_palindrome(i * j):
            palindrome.append(i * j)

print(max(palindrome))

# Answer - 906609
