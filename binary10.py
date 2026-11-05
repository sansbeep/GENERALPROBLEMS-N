class Data:
    def __init__(self, value, index, count=0):
        self.value = value
        self.index = index
        self.count = count
def sortByFrequency(arr):
    if arr is None or len(arr) < 2:
        return
    hm = {}
    for i in range(len(arr)):
        hm.setdefault(arr[i], Data(arr[i], i)).count += 1
    values = [*hm.values()]
    values.sort(key=lambda x: (-x.count, x.index))
    k = 0
    for data in values:
        for j in range(data.count):
            arr[k] = data.value
            k += 1
if __name__ == "__main__":
    arr = [5, 3, 1, 2, 2, 4, 5, 3]
    print("Original array:", arr)
    sortByFrequency(arr)
    print("Sorted array by frequency and index:", arr)