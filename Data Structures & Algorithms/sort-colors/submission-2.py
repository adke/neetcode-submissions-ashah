class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        countRed = 0
        countBlue = 0
        countWhite = 0

        for n in nums:
            if n == 0:
                countRed += 1
            elif n == 1:
                countWhite += 1
            else:
                countBlue += 1
        
        nums.clear()

        while countRed != 0:
            nums.append(0)
            countRed -= 1

        while countWhite != 0:
            nums.append(1)
            countWhite -= 1

        while countBlue != 0:
            nums.append(2)
            countBlue -= 1

        
