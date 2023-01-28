## Leetcode

def convert(n):
    s=str(n)
    s=s[::-1]
    result=".".join(s[i:i+3] for i in range(0,len(s),3))
    return result[::-1]
print(convert(1234567)) ##7654321
# 1.234.567
