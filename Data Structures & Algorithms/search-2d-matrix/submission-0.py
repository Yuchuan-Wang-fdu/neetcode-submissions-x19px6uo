class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r, c = len(matrix), len(matrix[0])

        t, b = 0, r-1

        while t<=b:
            m = (t+b)//2
            if matrix[m][0]> target:
                b = m - 1
            elif matrix[m][-1]< target:
                t = m + 1
            else:
                break
            
        if not (t<=b):
            return False
        m, n = 0, c -1
        r = (t+b)//2
        while m <= n:
            mid = (m+n)//2
            if matrix[r][mid]< target:
                m = mid + 1
            elif matrix[r][mid]> target:
                n = mid - 1
            else:
                return True
        return False



        