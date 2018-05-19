


def binary_search(arr, item):
    low = 0 
    high = len(arr) - 1
   # mid = (low+high) // 2
   
    #guess = arr[mid]

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        print(mid)
        if guess == item:
            return mid
        if guess > item : 
           high = mid - 1
        else: 
            low = mid + 1
        return None 

n1 = [1,2,3,4,5,6,7,8,9,10]
n = list(range(1, 10))
print(n1)
print(binary_search(n1, 8))


