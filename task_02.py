def count_inversions(data,x):
    def mergesort_counter(array):
        def merge(arr1, arr2):
            array = []
            i, o = 0, 0
            counter = 0
            while i < len(arr1) and o < len(arr2):
                if arr1[i] <= arr2[o]:
                    array.append(arr1[i])
                    i += 1
                else:
                    array.append(arr2[o])
                    counter += len(arr1[i:])
                    o += 1
            if i < len(arr1):
                array += arr1[i:]
            if o < len(arr2):
                array += arr2[o:]
            return array, counter


        counter = 0
        #print("Working ",array)
        if len(array)>1:
            mid = (int)(len(array)/2)
            larr = array[:mid]
            rarr = array[mid:]
            larr, lcount = mergesort_counter(larr)
            rarr, rcount = mergesort_counter(rarr)
            array, icount = merge(larr,rarr)
            counter = lcount + rcount + icount
        #print("Merged ",array)
        #print("Counter ",counter)
        return array, counter
    for i in range(1,len(data[x])):
        for o in range(i):
            if data[x][i-o]<data[x][i-o-1]:
                for p in range(len(data)):
                    data[p][i - o], data[p][i - o - 1] = data[p][i - o - 1], data[p][i - o]
            else:
                break
    counter = []
    #start = data.index(1)
    for i in range(len(data)):
     #   data[i] = data[i][start:]
      #  for elem in data[i]:
       #     if elem == 0:
        #        data[i].pop(data[i].index(elem))
        #if i != x:
        counter.append([i,mergesort_counter(data[i])[1]])
    return sorted(counter,key=(lambda x:x[1]))




data = [[3, 2, 10, 6, 9, 1, 5, 7, 4, 8],
        [2, 10, 8, 9, 5, 4, 3, 7, 6, 1],
        [2, 4, 9, 6, 10, 7, 5, 1, 3, 8],
        [3, 9, 10, 6, 7, 4, 1, 2, 5, 8],
        [7, 3, 8, 6, 5, 4, 10, 1, 2, 9]]
print(count_inversions(data,0))
