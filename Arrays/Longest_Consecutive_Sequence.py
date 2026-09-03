#Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

#define a class Solution with a method longestConsecutive 
#that takes a list of integers as input and returns an integer.
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
# Create a set from the input list.
        num_set = set(nums)
# Initialize the longest to keep track of the longest consecutive sequence.
        longest = 0
        for num in num_set:
# Check if the previous number is not in the set
# indicating the start of a new sequence.
            if num - 1 not in num_set:
# Initialize current to the current number and length to 1.
                current = num
                length = 1
#check whether the next consecutive number is in the set.
                while current + 1 in num_set:
# If it is present, increment current and length.
                    current += 1
                    length += 1
# Update longest if the current length is greater than the longest found
                longest = max(longest, length)
#return the longest consecutive sequence length found.
        return longest


#taking input from the user and converting it into a list of integers.
nums = list(map(int, input().split()))

#create an instance of the Solution class and call the longestConsecutive method with the input list.
solution = Solution()
print(solution.longestConsecutive(nums))