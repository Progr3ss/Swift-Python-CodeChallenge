
def missingNumber(nums):
    a = sorted(nums)
    for i in range(len(a)-1):
        if abs(a[i] - a[i+1]) == 2:
            return i+1

nums = [9,6,4,2,3,5,7,0,1]

print(missingNumber(nums))
