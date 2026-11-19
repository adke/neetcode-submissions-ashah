class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0
        twenty = 0

        for b in bills:
            if b == 5:
                five += 1
                continue
            else:
                if b == 10:
                    ten += 1
                elif b == 20:
                    twenty += 1
                change = b - 5 # either 5 or 15
                # 2 cases to handle here
                if change == 5:
                    if five > 0:
                        five -= 1
                    else:
                        return False
                else:
                    if five >= 3:
                        five -= 3
                    elif five > 0 and ten > 0:
                        five -= 1
                        ten -= 1
                    else:
                        return False

        return True

        