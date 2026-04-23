class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW, COL = len(matrix), len(matrix[0])

        up, down = 0, ROW-1

        while up <= down:
            mid = (up + down)//2
            if matrix[mid][0] > target:
                down = mid -1
            elif matrix[mid][-1] < target:
                up = mid + 1
            else:
                break
        
        if not (up <= down):
            return False
        
        row = (up + down)//2
        l, r = 0, COL-1
        while l <= r:
            m = (l+r)//2
            if matrix[row][m] > target:
                r = m -1
            elif matrix[row][m] < target:
                l = m + 1
            else:
                return True
        return False

        