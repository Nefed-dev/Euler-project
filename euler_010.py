# Сумма простых чисел меньше 10 равна 2 + 3 + 5 + 7 = 17.
# Найдите сумму всех простых чисел меньше двух миллионов.

# Решето Эратосфена

def get_primes(n):
  m = n+1
  numbers = [True] * m 
  for i in range(2, int(n**0.5 + 1)):
    if numbers[i]:
      for j in range(i*i, m, i):
        numbers[j] = False
  primes = []
  for i in range(2, m):
    if numbers[i]:
      primes.append(i)
  return primes


primes = get_primes(2000000)
print(sum(primes))

# Answer:142913828922