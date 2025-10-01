"""
Problem:
Given an array of integer nums and an integer target, 
return indices of two numbers such that they add up to target. 

You may assume that each input would have exactly one solution, 
and you may not use the same element twice

Come up with an algorithm that is less than O(n**2) time complexity
"""

"""
Thought Process:
Aim: Get indices of two numbers that sum up to the target

Brute Force:
- Find all possible num pairs
- Get each of their sum
- if sum  == target:
      return indices of each num in pair
  

Minimum length of nums is 2


"""
# def main():
#     nums = list(map(int, input().split()))
#     target = int(input())
#     soln = Solution()
#     print(soln.twoSum(nums, target))


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        for i in range(len(nums)):

            for j in  range(i + 1, len(nums)):

                if nums[i] + nums[j] == target:
                    return([i, j])


# if __name__ == "__main__":
#     main()
                

                
