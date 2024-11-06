array = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr

sorted_array = bubble_sort(array)

print("Sorted array:", sorted_array)
