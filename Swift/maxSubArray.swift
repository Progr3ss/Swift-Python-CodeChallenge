


func maxSubArray(_ nums: [Int])-> Int{

    guard nums.count > 1 else {
      return nums[0]
   }

   var  big = Int.min, sum = 0 

   for i in 0..<nums.count{
       sum = sum + nums[i]
      
       if nums[i] > sum {
        sum = nums[i]

       }
       print("sum \(sum) and big\(big)")  
       if sum > big {
          big = sum
       }
    }
   return big
}
var nums = [-1,2,3]

print(maxSubArray(nums))
