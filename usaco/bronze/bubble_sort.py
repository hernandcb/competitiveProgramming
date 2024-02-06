
def bubble_sort(arr):
    for i in range(len(arr)-1):
        swapped = False
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        if not swapped:
            return arr

arr = [1, 3, 5, 2, 4]
print(bubble_sort(arr))
