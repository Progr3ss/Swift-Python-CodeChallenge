

def largestSum(arr):
    
    curSum = arr[0]
    maxSum = arr[0]

    for i in arr[1:]:
        curSum = max(i, i+ curSum)
        maxSum = max(maxSum, curSum)
    return maxSum


n = [1,2,-1,3,4,10,10,-10,-1]

print(largestSum(n))
