"""
Problem: https://leetcode.com/problems/single-number/

Thought Process:
If ony one element occurs once, Why not store everything in a hashmap, 
Implementing a counter, then check for the one with 1 count

Analysis:
TC: O(2n)
SC: O(n / 2)

New Idea:
Instead of storing counts, if an element is in seen, remove it
Then we have only the unique number left

Analysis:
TC: O(n) as second for loop iterates only once
SC: O(n / 2) is rare to reach.  Average case would be better SC in new idea

LeetCode Suggestion:
Use O(1) space

Idea:
How do we use a constant space to keep track of this large numbers?

Is there a way to make the space used by the dicts constant regardless of any sixe of input (n)? 
    This would only occur if repeated elements were close to each other, then we can delete
    But the elements here are in a random order
    We would have to iterate through the list n times to see if the a number appears twice (TC becomes O(n**2))

Next Constant space is a var
    If we store the first val in a var, storing the second replaces the first
    We need a way for the val in the var to keep track of multiple elements.

    How about we keep adding?
    If your first and second are 3 and 4, your var is 7.  Buh 7 can also mean 5 and 2

    How about multiplication
    We can keep each number as a factor and divide when we see a number that it can be divided by
    This would only work if the elements dont share any factors

Leetcode Hint: Think of XOR (^) operation

    a ^ a = 0 where a is a number
    that means we can keep track through xor, while removing repeated elements

Pattern: Bitwise Manipulation





"""


#Hashing
class Solution:
    def singleNumber1(self, nums: list[int]) -> int:
        # Brute Force:
        seen = {}
        for i in range(1, len(nums)):
            if nums[i] not in seen:
                seen[nums[i]] = 1
            else:
                seen[nums[i]] += 1

        for num in seen:
            if seen[num] == 1:
                return num

    # Optimized Hashing
    def singleNumber2(self, nums: list[int]) -> int:
        # Brute Force:
        seen = {}
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen[nums[i]] = i
            else:
                del seen[nums[i]]

                
        for num in seen:
            print(num)

    #BIT Manipulation
    def singleNumber3(self, nums: list[int]) -> int:

        unique = nums[0]
        for i in range(1, len(nums)):
            unique = unique ^ nums[i]

        return unique

    
#Driver code
def main():
    nums = [4, 1, 2, 2, 1]
    soln = Solution()
    print(soln.singleNumber3(nums))

if __name__ == "__main__":
    main()

