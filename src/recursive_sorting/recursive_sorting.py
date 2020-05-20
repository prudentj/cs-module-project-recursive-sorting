# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB=None):
    # elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements
    merged_arr=[]
    # Your code here
    if arrB==None:
        return arrA
    while (len(arrA)>0 and len(arrB)>0):
        if arrA[0]>arrB[0]:
            merged_arr.append(arrB.pop(0))
        else:
            merged_arr.append(arrA.pop(0))
    # If A isn't empty, throw the rest onto merged
    if len(arrA)>0:
        merged_arr= merged_arr+arrA
    if len(arrB)>0:
        merged_arr= merged_arr+arrB
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # Your code here
    # I need to have floor division here
    # Return the middle of the array
    if (len(arr)==1):
        return arr
    mid = len(arr)//2 
    left = arr[:mid]
    right = arr[mid:]
    if len(left)>1:
        left = merge_sort(left)
    if len(right)>1:
        right = merge_sort(right)
    arr = merge(left,right)
    return arr



#     # If the direct merge is already sorted 
#     if (arr[mid] <= arr[startTwo]): 
#         return; 

def merge_in_place(arr, start, mid, right):
    # Your code here
    startTwo= mid + 1
    if (arr[mid] <= arr[startTwo]): 
        return arr
    
    while (start <= mid and startTwo <= right):
        if (arr[start] <= arr[startTwo]):
            start += 1
        else:
            swapped_item = arr[startTwo]
            index = startTwo
            while (index != start): 
                arr[index] = arr[index - 1] 
                index -= 1 
            
            arr[start] = swapped_item
            start += 1 
            mid += 1 
            startTwo += 1
    return arr


# left and right will need to be indexes
def merge_sort_in_place(arr, left, right):
    # Your code here
    if (left < right): 
        mid = left + (right - left) // 2 
        # sort one half then the other
        arr = merge_sort_in_place(arr, left, mid) 
        arr = merge_sort_in_place(arr, mid + 1, right) 

        arr = merge_in_place(arr, left, mid, right) 
    return arr

# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
