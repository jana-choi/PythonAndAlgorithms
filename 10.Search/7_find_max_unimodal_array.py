def find_max_unimodal_array(A):
    if len(A) <= 2:
        return None
    
    left = 0
    right = len(A) - 1

    while left + 1 < right:
        mid = (left + right) // 2

        if A[mid] > A[mid-1] and A[mid] > A[mid+1]:
            return A[mid]
        elif A[mid] > A[mid-1] and A[mid] < A[mid+1]:
            left = mid
        else:
            right = mid
    
    return None

def test_find_max_unimodal_array():
    seq = [1, 2, 5, 6, 7, 10, 12, 9, 8, 7, 6]
    print(find_max_unimodal_array(seq))
    print(max(seq))


if __name__ == "__main__":
    test_find_max_unimodal_array()