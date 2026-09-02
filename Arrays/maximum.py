#finding the maximum value in an array
#we define an array of numbers and initialize the maximum value to the first element of the array. 
#we then iterate through each number in the array,
#comparing it to the current maximum value. 
#if we find a number greater than the current maximum value,
#we update the maximum value. 
#finally, we print the maximum value found in the array.
arr = [10, 25, 36, -47, 58, 69, -80]
max_value = arr[0]
for num in arr:
    if num > max_value:
        max_value = num
print(max_value)