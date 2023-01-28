def peaks(arr):
    pos=[]
    prob_peak=False
    for i in range(1,len(arr)):
        if arr[i]>arr[i-1]:  ##eg [1,2,3,5,4]-->pos(1) and pos(0)-->2>1:prob_peak=1
            prob_peak=i ## True
        elif arr[i]<arr[i-1] and prob_peak:
            pos.append(prob_peak)
            prob_peak=False
    return {"pos":pos,"peak":[arr[i] for i in pos]}

print(peaks([1,2,3,6,4,1,2,3,2,1]))