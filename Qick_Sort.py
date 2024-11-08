def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)

try:
    user_input = input("Enter numbers separated by spaces: ")
    arr = list(map(int, user_input.split()))
    sorted_arr = quicksort(arr)
    print("Sorted array:", sorted_arr)
except ValueError:
    print("Please enter valid integers separated by spaces.")
