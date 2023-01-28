# cook your dish here
def solution():
    numList=[]
    T=int(input())
    for i in range(T):
        M,N=map(int,input().split())
        for i in range(M):
            A=list(map(int,input().split()))
            numList.append(A)
        m=0
        for i in numList:
            if i[0]<=N:
                m=max(m,i[1])
        print(m)
solution()

# for _ in range(int(input())):
#     n,x = map(int,input().split())
#     a = []
#     for i in range(n):
#         j = list(map(int,input().split()))
#         a.append(j)
#     m = 0
#     for i in a:
#         if i[0] <= x:
#             m = max(m,i[1])
#     print(m)