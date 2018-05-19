

def quicksort(array):
    if len(array) < 2:
        return array

    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)
b = [2,1]
a = [2,3,23,21,6,7,8,9,1,0]
print(quicksort(b))
