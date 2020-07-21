def sequential_search(seq, n):
    for item in seq:
        if item == n:
            return True
    return False

def test_sequential_search():
    seq = [1, 5, 6, 8, 3]
    n1 = 5
    n2 = 7
    print(sequential_search(seq, n1))
    print(sequential_search(seq, n2))


if __name__ == "__main__":
    test_sequential_search()