class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        print(-5 // 2)
        print(int(-5 / 2))


        for c in tokens:
            if c == "+":
                res = stack.pop() + stack.pop()
                stack.append(res)

            elif c == "*":
                res = stack.pop() * stack.pop()
                stack.append(res)

            elif c == "/":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(int(num2 / num1))
            
            elif c == "-":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2 - num1)

            else:
                stack.append(int(c))

        return stack[-1]

