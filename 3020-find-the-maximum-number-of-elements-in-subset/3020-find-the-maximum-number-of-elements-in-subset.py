from collections import Counter
from typing import List

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        count = Counter(nums)
        max_len = max(1, count[1] - (count[1] % 2 == 0) if count[1] > 0 else 1)
        
        seen = set()
        for x in count:
            if x == 1 or x in seen:
                continue
            
            curr = x
            curr_len = 0
            while count[curr] >= 2:
                curr_len += 2
                seen.add(curr)
                curr *= curr
            
            if count[curr] > 0:
                curr_len += 1
            else:
                curr_len -= 1
                
            max_len = max(max_len, curr_len)
            
        return max_len