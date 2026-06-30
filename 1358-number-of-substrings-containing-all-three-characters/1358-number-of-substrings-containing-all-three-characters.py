class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        last_seen = [-1, -1, -1]
        count = 0
        
        for i, char in enumerate(s):
            last_seen[ord(char) - 97] = i
            count += min(last_seen) + 1
            
        return count