def gnome_sort(seq):
    i = 0
    while i < len(seq):
        if i == 0 or seq[i-1] <= seq[i]:
            i += 1
        else:
            seq[i], seq[i-1] = seq[i-1], seq[i]
            i -= 1
    return seq

def test_gnome_sort():
    seq = [5, 3, 2, 4]
    print(gnome_sort(seq))
    print(sorted(seq))


if __name__ == "__main__":
    test_gnome_sort()