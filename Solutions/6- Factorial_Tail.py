def prime(n):
    for i in range(2,n):
        if n%i == 0: return False
    return True
primes = [x for x in range(2,257) if prime(x)]
def get_prime_divisors(n):
    dct = {}
    while n>1:
        for i in primes:
            if n%i == 0: dct[i], n = dct.get(i,0)+1, n//i
    return dct
def get_ns(number, n):
    cnt = 0
    while number > 1:cnt, number = cnt + number // n, number // n
    return cnt
def zeroes(base, number):
    divisors, numbers, minimum = get_prime_divisors(base), {}, 150**5
    for i in divisors:  numbers[i] = get_ns(number, i)
    for i in divisors:
        if numbers[i] // divisors[i] < minimum: minimum = numbers[i] // divisors[i]
    return minimum