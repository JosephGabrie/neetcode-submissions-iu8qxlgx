class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_area = 0
        width = 0
        area = 0
        min_height = 0
        while l < r:
            width = r - l
            area = min(heights[l], heights[r]) * width
            max_area = max(area, max_area)

            if heights[l] >= heights[r]:
                r -= 1
            elif heights[r] > heights[l]:
                l += 1
                width = r - l


        return max_area
