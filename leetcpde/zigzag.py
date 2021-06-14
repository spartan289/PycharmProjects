class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = ['' for i in range(numRows)]
        row = 0
        dir = -1
        for c in s:
            rows[row] += c
            if row == 0 or row == numRows - 1:
                dir *= -1
            row += dir
        return ''.join(rows)
l1 = Solution()
print(l1.convert("paypalishiring",3))
