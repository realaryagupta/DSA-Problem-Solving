# How do you reverse an array in place?

''' APPROACH -1 - Using an Extra array
'''

# Driver Code
arr = [ 1,6,3,4,5,6,7,8,9,0]

#  Function 
def reverse(arr):
    reverse_array = []
    for i in range(len(arr)):
        a = 9 - i
        reverse_array.append(arr[a])
    print(reverse_array)

reverse(arr)

# ________________________________________________

''' Using Reverse Function'''

arr.reverse()
print("Using reverse() ", arr)
print("Using reversed() ", list(reversed(arr)))
#  ________________________________________________










''' Using for loop and 2 pointer ( start and end ) interchange these 2 pointers. '''

def pointer(arr):
    for i in range(len(arr)):
        a = 0
        b = len(arr)
        
        arr[a] , arr[b] = arr[b], arr[a]
        a = a + 1
        b = b - 1
        print(arr)

#  pointer(arr)



