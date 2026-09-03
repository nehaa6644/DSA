#move all zeros to the end
def moveZeroes(nums): 
    insert_pos = 0 

    for i in range(len(nums)):
        if nums[i] != 0: 
# swap the current element with the element at insert_pos
            nums[insert_pos], nums[i] = nums[i], nums[insert_pos] 
# increment insert_pos to point to the next position for the next non-zero element
            insert_pos += 1

nums = list(map(int, input().split()))
moveZeroes(nums)
print(nums)