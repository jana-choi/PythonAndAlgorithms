def convert_from_decimal_larger_bases(number, base):
    strings = "0123456789ABCDEFGHIJ"
    result =""
    
    while number > 0:
        digit = number % base
        result = strings[digit] + result
        number = number // base
    
    return result

def test_convert_from_decimal_larger_bases():
    number = 31
    base = 16

    print("convert_from_decimal_larger_bases(number, base):", convert_from_decimal_larger_bases(number, base))


if __name__ == "__main__":
    test_convert_from_decimal_larger_bases()