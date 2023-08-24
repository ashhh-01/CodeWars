#Codechef

def solution():
    T=int(input())
    for i in range(T):
        N,S=map(int,input().split())
        T1=min(N,S)
        T2=T1-S
        diff=T1+T2
        print(diff)
    
solution()



