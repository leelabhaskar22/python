array=[1,3,5,34,45,56,89,93]

def BinarySearch(arr,key):
    low=0
    high=len(arr)
    while(low<=high):
        mid = int((low+high)/2)
        if(arr[mid] == key):
            return mid
        elif(arr[mid] < key):
            low= mid+1
        else:
            high=mid-1

result = BinarySearch(array,89)
print(f'Element Found at {result}')