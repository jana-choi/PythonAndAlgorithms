def convert_dec_to_any_base_rec(number, base):
    convertString = "0123456789ABCDEF"
    if number < base:
        return convertString[number]
    else:
        return convert_dec_to_any_base_rec(number // base, base) + convertString[number % base]
    
def test_convert_dec_to_any_base_rec():
    number = 9
    base = 2
    print("convert_dec_to_any_base_rec(number, base):", convert_dec_to_any_base_rec(number, base))


if __name__ == "__main__":
    test_convert_dec_to_any_base_rec()