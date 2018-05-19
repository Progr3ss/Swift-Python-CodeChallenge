


def pair_sum(arr, k):
    if len(arr) < 2:
        return 

    seen = set()
    output = set()

    for num in arr:
        target = k - num
 
        if target not in seen:
           seen.add(num)
           print()

        else:
            output.add((min(num,target), max(num, target)))
            

    return ''.join(map(str(output)))
arr = [1,3,2,2]

print(pair_sum(arr, 4))
