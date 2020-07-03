import numpy as np

def testing_numpy():
    # tests many features of numpy
    ax = np.array([1, 2, 3])
    ay = np.array([3, 4, 5])

    print("### 1")
    print(ax)
    
    print("### 2")
    print(ax*2)

    print("### 3")
    print(ax+10)

    print("### 4")
    print(np.sqrt(ax))

    print("### 5")
    print(np.cos(ax))

    print("### 6")
    print(ax-ay)

    print("### 7")
    print(np.where(ax<2, ax, 10))
    
    m = np.matrix([ax, ay, ax])
    print("### 8")
    print(m)

    print("### 9")
    print(m.T)

    grid1 = np.zeros(shape=(10,10), dtype=float)
    grid2 = np.ones(shape=(10,10), dtype=float)

    print("### 10")
    print(grid1)

    print("### 11")
    print(grid2)

    print("### 12")
    print(grid1[1]+10)

    print("### 13")
    print(grid2[:,2]*2)


if __name__ == "__main__":
    testing_numpy()