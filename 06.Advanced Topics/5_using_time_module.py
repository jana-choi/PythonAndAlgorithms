import time

def sumOfN2(n):
    start = time.time()
    theSum = 0
    for i in range(1, n+1):
        theSum = theSum + 1
    end = time.time()
    return theSum, end-start


if __name__ == "__main__":
    n = 500
    print("총 합계: %d\t 시간: %10.7f 초" % sumOfN2(n))
    n = 2000000
    print("총 합계: %d\t 시간: %10.7f 초" % sumOfN2(n))