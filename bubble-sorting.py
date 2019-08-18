arr = [7,1,4,1,2,9,3];
for i in range(0,len(arr)):
     for j in range(i+1,len(arr)):
            if arr[i] < arr[j]:
                inter = arr[j]
                arr[j] = arr[i]
                arr[i] = inter
                
for i in range(len(arr)):
    print (arr[i])
