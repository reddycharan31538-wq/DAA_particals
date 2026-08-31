print("=" * 50)
print("BUBBLE SORT ALGORITHM")
print("=" * 50)

n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    value = int(input(f"Enter element {i + 1}: "))
    arr.append(value)

print("\nOriginal Array:", arr)

# Bubble Sort
for i in range(n - 1):
    for j in range(n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print("Sorted Array:", arr)
print("=" * 50)