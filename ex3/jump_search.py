import math

def jump_search(arr, target):
    length = len(arr)
    step = int(math.sqrt(length))
    prev = 0
    
    while arr[int(min(step, length)-1)] < target:
        prev = step
        step += int(math.sqrt(length))
        if prev >= length:
            result = "No such nr in array"
            return result
    
    for i in range (prev, min(step, length)):
        if arr[i] == target:
            result = f"This nr exists in array on index {i}"
            return result
    result = "No such nr in array"
    return result

arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
target = 55

print(jump_search(arr, target))