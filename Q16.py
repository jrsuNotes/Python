def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1

def binary_search(lst, target):
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Example usage:
my_list = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target_num = int(input("Enter a number to search: "))

linear_search_index = linear_search(my_list, target_num)
binary_search_index = binary_search(my_list, target_num)

if linear_search_index != -1:
    print("Linear Search: Found at index", linear_search_index)
else:
    print("Linear Search: Not found")

if binary_search_index != -1:
    print("Binary Search: Found at index", binary_search_index)
else:
    print("Binary Search: Not found")
