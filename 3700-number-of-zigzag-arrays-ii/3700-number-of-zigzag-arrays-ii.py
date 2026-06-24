class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1

        def mul(A, B):
            C = [[0] * m for _ in range(m)]
            for i in range(m):
                row_a = A[i]
                row_c = C[i]
                for k in range(m):
                    if row_a[k]:
                        row_b = B[k]
                        for j in range(m):
                            row_c[j] = (row_c[j] + row_a[k] * row_b[j]) % MOD
            return C

        def power(A, p):
            res = [[1 if i == j else 0 for j in range(m)] for i in range(m)]
            base = A
            while p > 0:
                if p % 2 == 1:
                    res = mul(res, base)
                base = mul(base, base)
                p //= 2
            return res

        U = [[1 if i < j else 0 for j in range(m)] for i in range(m)]
        L = [[1 if i > j else 0 for j in range(m)] for i in range(m)]

        n -= 1
        UL = mul(U, L)
        P = power(UL, n // 2)

        if n % 2 == 1:
            P = mul(L, P)

        ans = sum(sum(row) % MOD for row in P) % MOD
        return (ans * 2) % MOD