def insertion_sort(seq):
    for i in range(1, len(seq)):
        j = i
        while j > 0 and seq[j-1] > seq[j]:
            seq[j-1], seq[j] = seq[j], seq[j-1]
            j -= 1
        print("[ing]:", seq)
    return seq

def insertion_sort_rec(seq, i=None):
    if i is None:
        i = len(seq)-1
    if i == 0:
        return i
    
    insertion_sort_rec(seq, i-1)
    
    j = i
    while j > 0 and seq[j-1] > seq[j]:
        seq[j-1], seq[j] = seq[j], seq[j-1]
        j -= 1
    return seq

def test_insertion_sort():
    seq = [11, 3, 28, 43, 9, 4]
    print(insertion_sort(seq))
    print(insertion_sort_rec(seq))
    print(sorted(seq))


if __name__ == "__main__":
    test_insertion_sort()