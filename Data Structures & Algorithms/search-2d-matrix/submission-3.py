class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        up, down = 0, row-1

        while up <= down:
            mid = (up+down)//2
            if matrix[mid][0] > target:
                down = mid -1
            elif matrix[mid][-1] <target:
                up = mid +1
            else:
                break

        if not (up <= down):
            return False

        rows = (up+down)//2
        l, r = 0, col-1

        while l<=r:
            m = (l+r)//2
            if matrix[rows][m]>target:
                r = m - 1
            elif matrix[rows][m]<target:
                l = m + 1
            else:
                return True

        return False 



        