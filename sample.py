print(1+2)
print("It is working..")
print(3+4)
print(6)
#updated in line 4

i=0
while(i<10):
   print(i)
  
 def partition(start, end, array):
      
    # Initializing pivot's index to start
    pivot_index = start 
    pivot = array[pivot_index]
      
    # This loop runs till start pointer crosses 
    # end pointer, and when it does we swap the
    # pivot with element on end pointer
    while start < end:
          
        # Increment the start pointer till it finds an 
        # element greater than  pivot 
        while start < len(array) and array[start] <= pivot:
            start += 1
              
        # Decrement the end pointer till it finds an 
        # element less than pivot
        while array[end] > pivot:
            end -= 1
          
        # If start and end have not crossed each other, 
        # swap the numbers on start and end
        if(start < end):
            array[start], array[end] = array[end], array[start]
      
    # Swap pivot element with element on end pointer.
    # This puts pivot on its correct sorted place.
    array[end], array[pivot_index] = array[pivot_index], array[end]
     
    # Returning end pointer to divide the array into 2
    return end
      
# The main function that implements QuickSort 
def quick_sort(start, end, array):
      
    if (start < end):
          
        # p is partitioning index, array[p] 
        # is at right place
        p = partition(start, end, array)
          
        # Sort elements before partition 
        # and after partition
        quick_sort(start, p - 1, array)
        quick_sort(p + 1, end, array)
          
# Driver code
array = [ 10, 6, 8, 9, 1, 5 ] #updated
quick_sort(0, len(array) - 1, array)
  
print(f'Sorted array: {array}')
printf("%d",5);


#Write KnapSack in Python
def knapSack(W, wt, val, n):
    if n == 0 or W == 0:
        return 0
    if (wt[n-1] > W):
        return knapSack(W, wt, val, n-1)
    else:
        return max(
            val[n-1] + knapSack(
                W-wt[n-1], wt, val, n-1),
            knapSack(W, wt, val, n-1))

val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print knapSack(W, wt, val, n)
