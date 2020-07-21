def ordered_squential_search(seq, n):
    for item in seq:
        if item > n:
            return False
        if item == n:
            return True
    return False

def test_ordered_sequential_search():
    seq = [1, 2, 4, 5, 6, 8, 10]
    n1 = 10
    n2 = 7
    print(ordered_squential_search(seq, n1))
    print(ordered_squential_search(seq, n2))


if __name__ == "__main__":
    test_ordered_sequential_search()