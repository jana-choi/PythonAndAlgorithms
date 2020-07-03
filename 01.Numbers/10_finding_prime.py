import math
import random

def finding_prime(number):
    num = abs(number)
    if num < 4:
        return True
    
    for x in range(2, num):
        if num % x == 0:
            return False
    
    return True

def finding_prime_sqrt(number):
    num = abs(number)
    if num < 4:
        return True
    
    for x in range(2, int(math.sqrt(number)) + 1):
        if num % x == 0:
            return False
    
    return True

def finding_prime_fermat(number):
    if number <= 102:
        for a in range(2, number):
            if pow(a, number-1, number) != 1:
                return False
        return True
    else:
        for i in range(100):
            a = random.randint(2, number-1)
            if pow(a, number-1, number) != 1:
                return False
        return True

def test_findiing_prime():
    number1 = 17
    number2 = 20

    print("finding_prime(number1):", finding_prime(number1))
    print("finding_prime(number2):", finding_prime(number2))
    print("finding_prime_sqrt(number1):", finding_prime_sqrt(number1))
    print("finding_prime_sqrt(number2):", finding_prime_sqrt(number2))
    print("finding_prime_fermat(number1):", finding_prime_fermat(number1))
    print("finding_prime_fermat(number2):", finding_prime_fermat(number2))


if __name__ == "__main__":
    test_findiing_prime()