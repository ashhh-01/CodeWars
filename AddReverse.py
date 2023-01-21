def add(l1,l2):
    n1=""
    n2=""
    numlist=[]
    for i in l1[::-1]:
        n1+=str(i)
    for i in l2[::-1]:
        n2+=str(i)
    sum=int(n1)+int(n2)
    for i in str(sum)[::-1]:
        numlist.append(int(i))
    return numlist

print(add([2,4,3],[5,6,4]))

## Example
## The given numbers in the list is reversed 
## n1=342
## n2=465
## The reversed numbers are added
# sum=807
## reversedNum=708
## Output : [7,0,8]