class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)

        stack = []
        area = 0

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                top = stack.pop()
                height = heights[top]
                left_smaller = stack[-1] if stack else -1
                width = i-left_smaller-1
                area = max(area, height*width)
            stack.append(i)
        return area

        