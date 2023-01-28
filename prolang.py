### codechef
## OOP

class Solution:
    def answer(self):
        T=int(input())
        for i in range(T):
            a,b,c,d,e,f=map(int,input().split())
            self.lang1=[c,d]
            self.lang2=[e,f]
            if a in self.lang1 and b in self.lang1:
                print(1)
            elif a in self.lang2 and b in self.lang2:
                print(2)
            else:
                print(0)
sol=Solution()
sol.answer()