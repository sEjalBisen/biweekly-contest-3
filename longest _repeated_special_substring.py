from collections import defaultdict
class solution:
    def longestSpecialSubstring(self, s):
        map = defaultdict(int)
        ans = -1
        
        for i in range(len(s)):
            ch = s[i]
            substring_len = 0
            
            for j in range(i, len(s)):
                if ch != s[j]:
                    break 
                substring_len += 1 
                
                key = (ch, substring_len)
                map[key] += 1 
                if map[key] >= 3:
                    ans = max(ans, substring_len)
                    
        return ans 
                
        
            