## Given an array arr of n elements that is first strictly increasing and then maybe strictly decreasing, find the maximum element in the array.

Note: If the array is increasing then just print the last element will be the maximum value.

Example:
Input: array[]= {5, 10, 20, 15}\
Output: 20\
Explanation: The element 20 has neighbors 10 and 15, both of them are less than 20.\

Input: array[] = {10, 20, 15, 2, 23, 90, 67}\
Output: 20 or 90\
Explanation: The element 20 has neighbors 10 and 15, both of them are less than 20, similarly 90 has neighbors 23 and 67.\

### Corner Cases
1. If the array is strictly increasing then the highest number will be the end of the array.
2. If the array is strictly decreasing then the highest number will be at the starting of the array.
3. If all the elements of an array are same then any value can be taken as the highest value of an array.

### Pseducode
Naive Approach: Below is the idea to solve the problem

The array can be traversed and the element whose neighbors are less than that element can be returned.

Follow the below steps to Implement the idea: 

- If the first element is greater than the second or the last element is greater than the second last, print the respective element and terminate the program.
- Else traverse the array from the second index to the second last index i.e. 1 to N – 1
- If for an element array[i] is greater than both its neighbors, i.e., array[i] > =array[i-1]  and array[i] > =array[i+1] , then print that element and terminate.



# Find the peak element in the array 
def findPeak(arr, n) : 

	# first or last element is peak element 
	if (n == 1) : 
	return 0
	if (arr[0] >= arr[1]) : 
		return 0
	if (arr[n - 1] >= arr[n - 2]) : 
		return n - 1

	# check for every other element 
	for i in range(1, n - 1) : 

		# check if the neighbors are smaller 
		if (arr[i] >= arr[i - 1] and arr[i] >= arr[i + 1]) : 
			return i 
			
# Driver code. 
arr = [ 1, 3, 20, 4, 1, 0 ] \
n = len(arr) \
print("Index of a peak point is", findPeak(arr, n)) 


