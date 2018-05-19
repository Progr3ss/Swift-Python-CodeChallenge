

def moveZeroes(nums):
    num1 = nums.count(0)
    for i in range(num1):
        print(i)
        nums.remove(0)
        nums.append(0)
        #if nums.contains(0):
         #   print(nums[i])
           # del nums[i]
            #del nums[i]
    
    return nums

nums = [0, 1, 0, 3, 12]
print(moveZeroes(nums))

