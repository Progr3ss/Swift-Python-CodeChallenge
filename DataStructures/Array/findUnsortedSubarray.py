
def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0 


    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i

    return smallest_index
def selectionSort(arr):
    newArr = []
    cnt = 0
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr



arr = [2,6,4,8,10,9,15]
print(selectionSort(arr))

#def findUnsortedSubarray(nums):
    
