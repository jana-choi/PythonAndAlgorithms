def convert_to_decimal(number, base):
    multiplier = 1
    result = 0

    while number > 0:
        result += number % 10 * multiplier
        multiplier *= base
        number = number // 10
    
    return result

def test_convert_to_decimal():
    number = 1001
    base = 2
    
    print("convert_to_decimal(number, base):", convert_to_decimal(number, base))
    assert(convert_to_decimal(number, base) == 9)
    print("테스트 통과!")


if __name__ == "__main__":
    test_convert_to_decimal()