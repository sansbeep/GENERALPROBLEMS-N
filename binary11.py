def sortArray(A):
    if len(A) <= 1:
        return
    x = -1
    y = -1
    prev = A[0]
    for i in range(1, len(A)):
        if prev > A[i]:
            if x == -1:
                x = i - 1
                y = i
            else:
                y = i
        prev = A[i]
    swap(A, x, y)
def swap(A, x, y):
    temp = A[x]
    A[x] = A[y]
    A[y] = temp
if __name__ == "__main__":
    A = [1, 3, 5, 3, 2, 4]
    print("Original array:", A)
    sortArray(A)
    print("Sorted array:", A)