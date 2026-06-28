from collections import deque
from typing import List

class Solution:
    def solve(self, n, l, r, penalty, pre):
        dp_sum = [0] * (n + 1)
        dp_cnt = [0] * (n + 1)

        dq = deque()

        for i in range(1, n + 1):
            j = i - l

            if j >= 0:
                while dq:
                    x = dq[-1]

                    v1 = dp_sum[x] - pre[x]
                    v2 = dp_sum[j] - pre[j]

                    if v2 > v1 or (v2 == v1 and dp_cnt[j] <= dp_cnt[x]):
                        dq.pop()
                    else:
                        break

                dq.append(j)

            while dq and dq[0] < i - r:
                dq.popleft()

            dp_sum[i] = dp_sum[i - 1]
            dp_cnt[i] = dp_cnt[i - 1]

            if dq:
                x = dq[0]

                ns = dp_sum[x] - pre[x] + pre[i] - penalty
                nc = dp_cnt[x] + 1

                if ns > dp_sum[i] or (ns == dp_sum[i] and nc < dp_cnt[i]):
                    dp_sum[i] = ns
                    dp_cnt[i] = nc

        return dp_sum[n], dp_cnt[n]

    def helper(self, n, l, r, pre):
        ans = -4 * 10 ** 18
        dq = deque()

        for i in range(1, n + 1):
            j = i - l

            if j >= 0:
                while dq and pre[dq[-1]] >= pre[j]:
                    dq.pop()

                dq.append(j)

            while dq and dq[0] < i - r:
                dq.popleft()

            if dq:
                ans = max(ans, pre[i] - pre[dq[0]])

        return ans

    def maximumSum(self, nums: List[int], m: int, l: int, r: int) -> int:
        n = len(nums)

        pre = [0] * (n + 1)
        for i in range(n):
            pre[i + 1] = pre[i] + nums[i]

        s, c = self.solve(n, l, r, 0, pre)

        if c == 0:
            return self.helper(n, l, r, pre)

        if c <= m:
            return s

        low = 0
        high = 2 * 10 ** 11
        ans = -4 * 10 ** 18

        while low <= high:
            mid = (low + high) // 2

            s, c = self.solve(n, l, r, mid, pre)

            if c <= m:
                ans = s + mid * m
                high = mid - 1
            else:
                low = mid + 1

        return ans