def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Check left child
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check right child
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not the root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        # Recursively heapify the affected subtree
        heapify(arr, n, largest)


def max_heap_sort(arr):
    n = len(arr)

    # Build Max Heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from heap
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]

        # Heapify reduced heap
        heapify(arr, i, 0)


# Main Program
print("=" * 60)
print("MAX-HEAP SORT ALGORITHM")
print("=" * 60)

arr = list(map(int, input("Enter elements separated by space: ").split()))

print("\nOriginal Array:", arr)

max_heap_sort(arr)

print("Sorted Array:", arr)

print("-" * 60)
print("Time Complexity: O(n log n)")
print("Space Complexity: O(log n) due to recursion")
print("=" * 60)