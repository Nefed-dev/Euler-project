# Простые делители числа 13195 - это 5, 7, 13 и 29.
# Каков самый большой делитель числа 600851475143, являющийся простым числом?
#
#
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?


num = 600851475143
count = 1
while num != 1:
    count += 1
    if num % count == 0:
        num /= count

print(count)
