def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

user_input = input("Enter the elements of the array separated by spaces: ")
arr = [int(x) for x in user_input.split()]

print("Original array:", arr)
insertion_sort(arr)
print("Sorted array:", arr)