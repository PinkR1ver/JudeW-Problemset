def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] >= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

def get_sorted_index_array(arr):
    n = len(arr)
    index_array = list(range(n))

    def custom_partition(low, high):
        i = low - 1
        pivot = arr[index_array[high]]

        for j in range(low, high):
            if arr[index_array[j]] <= pivot:
                i += 1
                index_array[i], index_array[j] = index_array[j], index_array[i]

        index_array[i + 1], index_array[high] = index_array[high], index_array[i + 1]
        return i + 1

    def custom_quicksort(low, high):
        if low < high:
            pi = custom_partition(low, high)
            custom_quicksort(low, pi - 1)
            custom_quicksort(pi + 1, high)

    custom_quicksort(0, n - 1)
    return index_array

# 示例
arr = [5, 2, 9, 1, 5, 6]
sorted_index = get_sorted_index_array(arr)
print("原始数组:", arr)
print("从大到小索引顺序:", sorted_index)
print("从大到小排序后的数组:", [arr[i] for i in sorted_index])
