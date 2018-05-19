

def maxSubArray(a):
    curSum = maxSum = a[0]
    for num in a[1:]:
        curSum = max(num, curSum + num)
        maxSum = max(maxSum, curSum)

    return maxSum


a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubArray(a))
