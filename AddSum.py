class Solution:
    def addsums(self,number,target):
        ## finds the index of the numbers in the list which when added together gives the target 
        numIndex={}  ## Stores as number:index
        for i in range(len(number)):
            if target-number[i] in numIndex:
                return [numIndex[target-number[i]],i]  ##return as a list
            numIndex[number[i]]=i 
        return []

add=Solution()
print(add.addsums([1,2,3,4,5,6,7,8],10))     
 ## output: [3, 5]
