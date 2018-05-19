



def rotate(nums, k):
    l = len(nums)
    s = []
    k = k%l

    for i in range(k):
        s.insert(0,nums[l-i-1])
    for j in range(k,l):
        s.append(nums[k-k])
    for m in range(l):
        nums[m] = s[m]

    return

nums = [1,2,3,4,5,6,7]
k = 3
print(rotate(nums,k))
