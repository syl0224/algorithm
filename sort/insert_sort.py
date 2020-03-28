class InsertSort(object):
    @classmethod
    def insert_sort(cls, arr):
        if arr == [] or arr is None:
            return []
        for i in range(0, len(arr)):
            pre_index = i - 1
            current = arr[i]
            while pre_index >= 0 and arr[pre_index] > current:
                arr[pre_index+1] = arr[pre_index]
                pre_index -= 1

            arr[pre_index+1] = current
        return arr


if __name__ == "__main__":
    arr = [3, 2, 5, 3, 8, 9, 6, 12, 14, 11]
    print(InsertSort.insert_sort(arr))
