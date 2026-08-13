import time


# Linear Search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# Binary Search
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# Main Program
print("=" * 60)
print("LINEAR SEARCH AND BINARY SEARCH")
print("=" * 60)

arr = list(map(int, input("Enter elements separated by space: ").split()))
target = int(input("Enter element to search: "))

# Binary Search requires a sorted array
sorted_arr = sorted(arr)

print("\nOriginal Array :", arr)
print("Sorted Array   :", sorted_arr)
print("Search Element :", target)

# Linear Search Time
start = time.perf_counter()
linear_result = linear_search(arr, target)
linear_time = time.perf_counter() - start

# Binary Search Time
start = time.perf_counter()
binary_result = binary_search(sorted_arr, target)
binary_time = time.perf_counter() - start

# Results
print("\n" + "-" * 60)

if linear_result != -1:
    print(f"Linear Search  : Element found at index {linear_result}")
else:
    print("Linear Search  : Element not found")

if binary_result != -1:
    print(f"Binary Search  : Element found at index {binary_result}")
else:
    print("Binary Search  : Element not found")

print("-" * 60)

print(f"Linear Search Time : {linear_time:.10f} seconds")
print(f"Binary Search Time : {binary_time:.10f} seconds")

print("\nTime Complexity:")
print("Linear Search  : Best O(1), Average O(n), Worst O(n)")
print("Binary Search  : Best O(1), Average O(log n), Worst O(log n)")

print("=" * 60)