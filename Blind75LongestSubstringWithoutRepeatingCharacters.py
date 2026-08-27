class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length_string = len(s)
        
        if length_string == 0:
            return 0 
        
        low, max_length = 0, 0
        cur_unique_chars = {}

        for high, char in enumerate(s):
    
            if char in cur_unique_chars and cur_unique_chars[char] >= low:
                low = cur_unique_chars[char] + 1
    
            
            cur_unique_chars[char] = high

            if high - low + 1 > max_length:
                max_length = high - low + 1
            
   
        return max_length