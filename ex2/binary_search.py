# l - left
# r - right
# x - element you are searching for

def binary_search(arr, l, r, x):
    while l <= r:
        # (r-l) - current search interval
        # (r-l)//2 - finds the middle point of the interval NB! floor division
        # l + (r-l)//2 - finds the index of subarry mid point in the entire array
        mid = l + (r - l) // 2
        if arr[mid] == x:
            result = f"The number '{x}' exists in the array."
            return result

        # if x is greater, ignore left half
        elif arr[mid] < x:
            l = mid + 1

        # if x is smaller, ignore right half
        else:
            r = mid - 1

    # if we reach here, then the element was not present
    result = "No such number in the array."
    return result
