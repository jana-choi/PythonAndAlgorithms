import math

def find_fibonacci_seq_iter(n):
    print("find_fibonacci_seq_iter()")
    if n < 2:
        return n

    a = 0
    b = 1
    for i in range(n):
        # a, b = b, a + b
        old_b = b
        b = a + b
        a = old_b
        print("i: {0}, a: {1}, b: {2}".format(i, a, b))
    
    return a

def find_fibonacci_seq_rec(n):
    if n < 2:
        return n
    return find_fibonacci_seq_rec(n - 1) + find_fibonacci_seq_rec(n - 2)

def find_fibonacci_seq_form(n):
    sq5 = math.sqrt(5)
    phi = (1 + sq5) / 2
    return int(math.floor(phi ** n / sq5))

def test_find_fib():
    n = 10
    print("find_fibonacci_seq_rec(n):", find_fibonacci_seq_rec(n))
    print("find_fibonacci_seq_iter(n):", find_fibonacci_seq_iter(n))
    print("find_fibonacci_seq_form(n):", find_fibonacci_seq_form(n))


if __name__ == "__main__":
    test_find_fib()