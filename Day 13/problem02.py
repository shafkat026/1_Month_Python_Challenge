# Custom Sorting Without sorted() 

# Given a list of numbers, sort it in ascending order without using built-in sorting functions.

# 👉 Bonus:

# Try implementing Bubble Sort or Selection Sort
# Then modify it to sort in descending order


arr = [5, 2, 9, 1, 7]

n = len(arr)
for i in range(n):
    for j in range(0, n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print("Ascending:", arr)

# Descending
arr.reverse()
print("Descending:", arr)