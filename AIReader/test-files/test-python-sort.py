def bubble_sort(arr):
    """Bubble sort algorithm - O(n^2) time complexity"""
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def binary_search(arr, target):
    """Binary search algorithm - O(log n) time complexity"""
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

# Test the functions
numbers = [64, 34, 25, 12, 22, 11, 90]
print("Original array:", numbers)

sorted_numbers = bubble_sort(numbers.copy())
print("Sorted array:", sorted_numbers)

target = 22
index = binary_search(sorted_numbers, target)
print(f"Element {target} found at index: {index}")
