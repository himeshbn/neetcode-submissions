class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        
        t_count = {}
        for char in t:
            t_count[char] = t_count.get(char, 0) + 1
        
        have = 0
        need = len(t_count)
        left = 0
        window_count = {}
        res = [-1, -1]
        res_len = float('inf')

        for right in range(len(s)):
            window_count[s[right]] = window_count.get(s[right],0)+1

            if s[right] in t_count and window_count[s[right]] == t_count[s[right]]:
                have += 1
            
            while have == need:
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1
                
                left_char = s[left]
                window_count[left_char] -= 1

                if left_char in t_count and window_count[left_char] < t_count[left_char]:
                    have -= 1

                left += 1

            l,r = res
        return s[l:r+1] if res_len != float('inf') else ""
