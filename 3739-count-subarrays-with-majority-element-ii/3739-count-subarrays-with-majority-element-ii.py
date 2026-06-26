class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        bit = [0] * (2 * n + 2)
        
        def add(idx: int, val: int):
            while idx < len(bit):
                bit[idx] += val
                idx += idx & (-idx)
                
        def query(idx: int) -> int:
            res = 0
            while idx > 0:
                res += bit[idx]
                idx -= idx & (-idx)
            return res

        offset = n + 1
        add(offset, 1)
        
        ans = 0
        curr_sum = 0
        
        for num in nums:
            if num == target:
                curr_sum += 1
            else:
                curr_sum -= 1
            
            ans += query(curr_sum + offset - 1)
            add(curr_sum + offset, 1)
            
        return ans