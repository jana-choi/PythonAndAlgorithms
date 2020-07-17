import heapq

def merge_sorted_seqs(seq1, seq2):
    result = []
    for c in heapq.merge(seq1, seq2):
        result.append(c)
    return result

def test_merge_sorted_seqs():
    seq1 = [1, 2, 3, 8, 9, 10]
    seq2 = [2, 3, 4, 5, 6, 7, 9]
    seq3 = seq1 + seq2
    
    print(seq3)
    print(sorted(seq3))
    print(merge_sorted_seqs(seq1, seq2))


if __name__ == "__main__":
    test_merge_sorted_seqs()