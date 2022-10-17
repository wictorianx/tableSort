

import time
import random
x = [3,7,4,9]
for i in range(10000):
    x.append(random.randint(1,1500))




def tableSort(x):
    len_x = len(x)
    t = {}
    max_yet = 0
    reps = 0
    for i in x:
        if i not in t:
            t[i] = 1
        else:
            t[i]+=1
            reps += 2
        if i > max_yet:
            max_yet = i
    o = []
    for i in range(max_yet+reps+1):
        o.append([])
    #print(o)
    reps_iter = 0
    for l in t:
        o[l+reps_iter] = l
        #print(o)
        #print(l)
        for j in range(t[l]-1):
            o[l+j+reps_iter+1] = l
            reps_iter +=1
    while True:
        try:
            o.remove([])
        except:
            #print(o)
            break
t0 = time.time()        
tableSort(x)
print(f"elapsed time: {time.time()-t0}")
def tim(x):
    MINIMUM= 32
      
    def find_minrun(n): 
      
        r = 0
        while n >= MINIMUM: 
            r |= n & 1
            n >>= 1
        return n + r 
      
    def insertion_sort(array, left, right): 
        for i in range(left+1,right+1):
            element = array[i]
            j = i-1
            while element<array[j] and j>=left :
                array[j+1] = array[j]
                j -= 1
            array[j+1] = element
        return array
                  
    def merge(array, l, m, r): 
      
        array_length1= m - l + 1
        array_length2 = r - m 
        left = []
        right = []
        for i in range(0, array_length1): 
            left.append(array[l + i]) 
        for i in range(0, array_length2): 
            right.append(array[m + 1 + i]) 
      
        i=0
        j=0
        k=l
       
        while j < array_length2 and  i < array_length1: 
            if left[i] <= right[j]: 
                array[k] = left[i] 
                i += 1
      
            else: 
                array[k] = right[j] 
                j += 1
      
            k += 1
      
        while i < array_length1: 
            array[k] = left[i] 
            k += 1
            i += 1
      
        while j < array_length2: 
            array[k] = right[j] 
            k += 1
            j += 1
      
    def tim_sort(array): 
        n = len(array) 
        minrun = find_minrun(n) 
      
        for start in range(0, n, minrun): 
            end = min(start + minrun - 1, n - 1) 
            insertion_sort(array, start, end) 
       
        size = minrun 
        while size < n: 
      
            for left in range(0, n, 2 * size): 
      
                mid = min(n - 1, left + size - 1) 
                right = min((left + 2 * size - 1), (n - 1)) 
                merge(array, left, mid, right) 
      
            size = 2 * size 
      
      
      
      
    array = x 
      
    print("Array:") 
    #print(array) 
      
    tim_sort(array) 
      
    print("Sorted Array:") 
    #print(array)
t1 = time.time()        
tim(x)
print(f"elapsed time: {time.time()-t1}")