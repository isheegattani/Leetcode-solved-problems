class Solution:
    def checkValidString(self, s: str) -> bool:
        stack=[]
        star=[]
        for i,v in enumerate(s):
            if v=="(":
                stack.append(i)
            elif v==")":
                if len(stack)>0:
                    stack.pop()
                elif len(star)>0:
                    star.pop()
                else:
                    return False
            else:
                star.append(i)
        while stack and star:
            if stack[-1]<star[-1]:
                stack.pop()
                star.pop()
            else:
                break
        return len(stack)==0
