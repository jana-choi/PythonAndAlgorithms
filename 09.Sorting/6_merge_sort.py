def merge_sort(seq):
    # (1) pop() 을 이용한 병합 정렬

    if len(seq) < 2:
        return seq

    mid = len(seq) // 2
    left, right = seq[:mid], seq[mid:]

    if len(left) > 1:
        left = merge_sort(left)
    if len(right) > 1:
        right = merge_sort(right)
    
    res = []
    while left and right:
        if left[-1] >= right[-1]:
            res.append(left.pop())
        else:
            res.append(right.pop())
    res.reverse()

    return (left or right) + res

def merge_sort_seq(seq):
    # (2) 두 함수로 나누어서 구현한다.
    # 한 함수에서는 배열을 나누고,
    # 또 다른 함수에서는 배열을 병합한다.
    
    if len(seq) < 2:
        return seq
    
    mid = len(seq) // 2
    left = merge_sort_seq(seq[:mid])
    right = merge_sort_seq(seq[mid:])

    return merge(left, right)

def merge(left, right):
    if not left or not right:
        return left or right
    
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        
    if left[i:]:
        result.extend(left[i:])
    if right[j:]:
        result.extend(right[j:])
    
    return result

def merge_2n(left, right):
    # 각 두 배열은 정렬된 상태다.
    # 시간 복잡도는 O(2n) 이다.

    if not left or not right:
        return left or right
    
    result = []
    while left and right:
        if left[-1] >= right[-1]:
            result.append(left.pop())
        else:
            result.append(right.pop())
    result.reverse()

    return (left or right) + result

def merge_two_arrays_inplace(l1, l2):
    # (4) 제자리 정렬로 구현한다.
    if not l1 or not l2:
        return l1 or l2
    
    p2 = len(l2) - 1
    p1 = len(l1) - len(l2) - 1
    p12 = len(l1) - 1

    while p2 >= 0 and p1 >= 0:
        item_to_be_merged = l2[p2]
        item_bigger_array = l1[p1]
        if item_to_be_merged < item_bigger_array:
            l1[p12] = item_bigger_array
            p1 -= 1
        else:
            l1[p12] = item_to_be_merged
            p2 -= 1
        p12 -= 1
    
    return l1

def merge_files(list_files):
    # (5) 파일을 병합한다.

    result = []
    final = []
    for filename in list_files:
        aux = []
        with open(filename, "r", encoding="UTF-8") as file:
            for line in file:
                aux.append(int(line))
        result.append(aux)
    
    final.extend(result.pop())
    for l in result:
        final = merge(l, final)
    
    return final

def test_merge_sort():
    seq = [3, 5, 2, 6, 8, 1, 0, 3, 5, 6, 2]
    seq_sorted = sorted(seq)
    print("============================================")
    print("sorted(seq):", seq_sorted)
    print("merge_sort(seq):", merge_sort(seq))
    print("merge_sort_seq(seq):", merge_sort_seq(seq))

    l1 = [1, 2, 3, 4, 5, 6, 7]
    l2 = [2, 4, 5, 8]
    l_sorted = [1, 2, 2, 3, 4, 4, 5, 5, 6, 7, 8]
    print("============================================")
    print("l_sorted:", l_sorted)
    print("merge_2n(l1, l2):", merge_2n(l1, l2))

    l1 = [1, 2, 3, 4, 5, 6, 7, 0, 0, 0, 0]
    l2 = [2, 4, 5, 8]
    print("============================================")
    print("l_sorted:", l_sorted)
    print("merge_two_arrays_inplace(l1, l2):", merge_two_arrays_inplace(l1, l2))

    list_files = ["a.dat", "b.dat", "c.dat"]
    l_sorted = [1, 1, 2, 3, 3, 3, 4, 5, 5, 5, 6, 7, 8]
    print("============================================")
    print("l_sorted:", l_sorted)
    print("merge_files(list_files):", merge_files(list_files))


if __name__ == "__main__":
    test_merge_sort()