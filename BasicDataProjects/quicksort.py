def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]

    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x> pivot]

    return quicksort(left) + [pivot] + quicksort(right)

data = [56,89,35,2,3,46,98]

sorteddata = quicksort(data)
print ("SORTED DATA IS :" ,sorteddata)
print (60*"-")
# print(sorteddata)