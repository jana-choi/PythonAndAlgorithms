def remove_dup(l1):
    # 리스트의 중복된 항목을 제거한 후 반환한다.
    return list(set(l1))

def intersection(l1, l2):
    # 교집합 결과를 반환한다.
    return list(set(l1) & set(l2))

def union(l1, l2):
    # 합집합 결과를 반환한다.
    return list(set(l1) | set(l2))

def test_sets_operations_with_lists():
    l1 = [1, 2, 3, 4, 5, 5, 9, 11, 11, 15]
    l2 = [4, 5, 6, 7, 8]
    l3 = []

    print(remove_dup(l1))
    print(intersection(l1, l2))
    print(union(l1, l2))
    print(remove_dup(l3))
    print(intersection(l3, l2))
    print(sorted(union(l3, l2)))

if __name__ == "__main__":
    test_sets_operations_with_lists()