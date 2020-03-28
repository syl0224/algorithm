class QuickSort(object):
    @classmethod
    def quick_sort(cls, arr, left, right):
        if left < right:
            index = cls.ajust_arr(arr, left, right)
            cls.quick_sort(arr, left, index - 1)
            cls.quick_sort(arr, index + 1, right)
        return arr

    @classmethod
    def ajust_arr(cls, arr, left, right):
        i = left
        j = right
        x = arr[i]
        while i < j:
            while i < j and arr[j] >= x:
                j -= 1
            if i < j:
                arr[i] = arr[j]
                i += 1

            while i < j and arr[i] <= x:
                i += 1
            if i < j:
                arr[j] = arr[i]
                j -= 1
        arr[i] = x
        return i


if __name__ == "__main__":
    arr = [3, 2, 5, 3, 8, 9, 6, 12, 14, 11]
    print(QuickSort.quick_sort(arr, 0, len(arr) - 1))
