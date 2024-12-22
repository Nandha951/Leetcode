def binary_search(arr, target, start, end):

    if start > end:
        return "Not Found"
    middle = (start+end)//2

    # print(arr, target, arr[middle], start, end)

    if arr[middle] == target:
        print(f'Found at {middle} index')
    if arr[middle] > target:
        binary_search(arr, target, start, middle-1)
    if arr[middle] < target:
        binary_search(arr, target, middle+1, end)

arr = [1,2,3,4,5,6,7,8,9,10]
target = 2
binary_search(arr, target, 0, len(arr))