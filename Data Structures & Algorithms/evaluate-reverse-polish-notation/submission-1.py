class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for n in tokens:
            if n in "+-*/":
                a = stack.pop()
                b = stack.pop()
                if n == "+":
                    stack.append(b+a)
                elif n == "-":
                    stack.append(b-a)
                elif n == "*":
                    stack.append(b*a)
                else:
                    stack.append(int(float(b)/a))
            else:
                stack.append(int(n))
        return stack[0]     


          