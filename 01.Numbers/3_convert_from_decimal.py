def convert_from_decimal(number, base):
    multiplier = 1
    result = 0

    while number > 0:
        result += number % base * multiplier
        multiplier *= 10
        number = number // base
    
    return result

def test_convert_from_decimal():
    number = 9
    base = 2

    print("convert_from_decimal(number, base):", convert_from_decimal(number, base))


if __name__ == "__main__":
    test_convert_from_decimal()