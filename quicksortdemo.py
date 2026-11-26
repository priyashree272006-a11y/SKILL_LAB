count=0
def quick_sort(arr):
 global count
 if len(arr)<=1:
   return arr
 pivot=arr[0]
 left=[]
 right=[]
 for i in range(1,len(arr)):
   count+=1
   if arr[i]<pivot:
     left.append(arr[i])
   else:
     right.append(arr[i])
 return quick_sort(left)+[pivot]+quick_sort(right)
arr=list(map(int, input("enter array elements:").split()))
sorted_arr=quick_sort(arr) 
print("sorted array:",sorted_arr)
print("number of iterations:",count)    
                 