def bruteforce(nums):
    maxSum = nums[0]
    for i in range(len(nums)):
        curSum = 0
        for j in range(i,len(nums)):
            curSum += nums[j]
            maxSum = max(maxSum, curSum)

    return maxSum

nums = [4,-1,2,-7,3,4]
res =bruteforce(nums)
print(res)