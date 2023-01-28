from collections import Counter
class Solution:
    def answer(self,String=input()):
        for i,e in Counter(String).items():
            print(f"{i}{e}",end="")

sol=Solution()
sol.answer()