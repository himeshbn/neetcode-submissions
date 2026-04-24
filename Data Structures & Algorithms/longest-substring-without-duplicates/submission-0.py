class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_seen = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            while s[right] in char_seen:
                char_seen.remove(s[left])
                left += 1 
            
            char_seen.add(s[right])

            max_length = max(max_length, right-left+1)
        return max_length
