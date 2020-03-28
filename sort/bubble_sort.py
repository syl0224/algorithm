class BubbleSort(object):
    @classmethod
    def bubble_sort(cls, arr):
        if arr == [] or arr is None:
            return []
        for i in range(0, len(arr)):
            for j in range(0, len(arr)-i-1):
                if arr[j] > arr[j+1]:
                    tmp = arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1] = tmp
        return arr


if __name__ == "__main__":
    arr = [3, 2, 5, 3, 8, 9, 6, 12, 14, 11]
    print(BubbleSort.bubble_sort(arr))
