def linear_search(arr, N, x):
    for nr in range(0, N):
        if arr[nr] == x:
            result = f"The number '{x}' exists in the array."
            return result
    result = "No such number in the array."
    return result

arr = [1, 2, 3, 7, 15, 4, 40]
x = 15
N = len(arr)

print(linear_search(arr, N, x))
