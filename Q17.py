# Insertion Sort
def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > key:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key

# Bubble Sort
def bubble_sort(lst):
    n = len(lst)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

# Selection Sort
def selection_sort(lst):
    for i in range(len(lst)):
        min_index = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]

# Example usage:
my_list = [5, 2, 9, 1, 7, 3]

print("Original List:", my_list)

insertion_sort(my_list)
print("After Insertion Sort:", my_list)

my_list = [5, 2, 9, 1, 7, 3]

bubble_sort(my_list)
print("After Bubble Sort:", my_list)

my_list = [5, 2, 9, 1, 7, 3]

selection_sort(my_list)
print("After Selection Sort:", my_list)
