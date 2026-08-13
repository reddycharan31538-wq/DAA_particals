print("=" * 50)
print("INSERTION SORT ALGORITHM")
print("=" * 50)

arr = list(map(int, input("Enter number of elements: ").split()))

print("\nOriginal Array:", arr)

for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1

    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = key

print("Sorted Array:", arr)
print("=" * 50)