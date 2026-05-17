def two_sum(nums, target):
    # step1 do sort
    nums.sort()
    result = []
    n = len(nums)
    # step2 N-2 nested loops (for 2sum 0 Nested loops)

    left = 0
    right = n-1

    # remaining_target = target - nums[i] # here no nested loops for iterating for 2sum so no remaining target direct target
    while left<right:
        two_sum = nums[left] + nums[right]

        if two_sum == target:
            result.append([nums[left], nums[right]])

            while left < right and nums[left] == nums[left+1]:
                left += 1
            while left < right and nums[right] == nums[right-1]:
                right -= 1
            left+=1
            right-=1
        elif two_sum < target:
            left+=1
        else:
            right-=1
    return result

print(two_sum([2,-4,5,6,2,0,1], 4))