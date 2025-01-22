# 这题就不是一个单纯的算法题，数学上是一个状态转移的问题
# https://leetcode.com/problems/student-attendance-record-ii/solutions/415467/python-o-log-n-using-numpy/
import numpy as np

class Solution:
    
    def checkRecord(self, n: int) -> int:
        MODULUS = 10**9 + 7

        initial_counts = np.array(
            [1, 0, 0, 0, 0, 0], 
            dtype=np.int64
        )

        adjacency_matrix = np.array([
            [1, 1, 1, 0, 0, 0],
            [1, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1],
            [0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0],
        ], dtype=np.int64)

        def power(A, exp): #这里利用了binary每一个位都始终是2^n
            B = np.identity(len(A), dtype=np.int64)
            for bit in reversed(bin(exp)[2:]):
                if bit == '1':
                    B = B @ A
                    B %= MODULUS
                A = A @ A
                A %= MODULUS
            return B

        final_counts = power(adjacency_matrix, n) @ initial_counts

        return sum(final_counts) % MODULUS