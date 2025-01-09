
def maxCrossingSum(arr, l, m, h): 

	sm = 0
	left_sum = -1000000

	for i in range(m, l-1, -1): 
		sm = sm + arr[i] 

		if (sm > left_sum): 
			left_sum = sm 

	# Include elements on right of mid 
	sm = 0
	right_sum = -1000000
	for i in range(m, h + 1): 
		sm = sm + arr[i] 

		if (sm > right_sum): 
			right_sum = sm 

	
	return max(left_sum + right_sum - arr[m], left_sum, right_sum) 



def maxSubArraySum(arr, l, h):  
	if (l > h): 
		return -10000
	# Base Case: Only one element 
	if (l == h): 
		return arr[l] 

	# Find middle point 
	m = (l + h) // 2

	# Return maximum of following three possible cases 
	# a) Maximum subarray sum in left half 
	# b) Maximum subarray sum in right half 
	# c) Maximum subarray sum such that the 
	#	 subarray crosses the midpoint 
	return max(maxSubArraySum(arr, l, m-1), 
			maxSubArraySum(arr, m+1, h), 
			maxCrossingSum(arr, l, m, h)) 


# Driver Code 
arr = [2, 3, 4, 5, -7,100] 
n = len(arr) 

max_sum = maxSubArraySum(arr, 0, n-1) 
print("Maximum contiguous sum is ", max_sum) 

# This code is contributed by Nikita Tiwari. 
