class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count0 = 0
        count1 = 0
        count2 = 0

        for n in nums:
            if n == 0:
                count0 += 1
            elif n == 1:
                count1 += 1
            else:
                count2 += 1
        
        nums.clear()

        while count0 != 0:
            nums.append(0)
            count0 -= 1
        
        while count1 != 0:
            nums.append(1)
            count1 -= 1

        while count2 != 0:
            nums.append(2)
            count2 -= 1

        





        