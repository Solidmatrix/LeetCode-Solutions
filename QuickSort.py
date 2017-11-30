def median(a,start,end):  
    center = (start+end)/2  
    if a[start] > a[center]:  
        a[start], a[center] = a[center], a[start]  
    if a[start] > a[end]:  
        a[start], a[end] = a[end], a[start]  
    if a[center] > a[end]:  
        a[center], a[end] = a[end], a[center]  
    a[start], a[center] = a[center], a[start]

def doSwap(a, start, end):
    if start >= end:
        return
    i, j = start, end
    #median(a, start, end)  
    tmp = a[start]  
    while True:  
        while a[j] > tmp and i < j:  
            j -= 1  
        if i < j:  
            a[i] = a[j]  
            i += 1
        while a[i] < tmp and i < j:  
            i += 1
        if i < j:
            a[j] = a[i]
            j -= 1
        else:  
            break  
    a[i] = tmp  
    doSwap(a, start, i-1)  
    doSwap(a, j+1, end)  

nums = [4,3,6,2,8,9,0]
doSwap(nums, 0, 6)
print nums