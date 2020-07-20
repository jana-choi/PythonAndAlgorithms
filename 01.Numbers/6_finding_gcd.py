def finding_gcd(a, b):
    print("finding_gcd({0}, {1})".format(a, b))

    while(b != 0):
        result = b
        a, b = b, a % b
        # old_b = b
        # b = a % b
        # a = old_b
        print("result:", result, "/ a:", a, "/ b:", b)
    
    # return result
    return a

def test_finding_gcd():
    number1 = 21
    number2 = 12
    print("finding_gcd(number1, number2):", finding_gcd(number1, number2))
    print("finding_gcd(number2, number1):", finding_gcd(number2, number1))


if __name__ == "__main__":
    test_finding_gcd()