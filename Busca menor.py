# Function to check the smallest element in an array

def Smallest_element(arr):
    smallest = arr[0] # Store the smallest value
    smallest_index = 0 # Stores the index of the smallest value

    for i in range(1,len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

# Sort by selection. Using the function above

def Sort_Selection(arr):
    New_arr = []
    for i in range(len(arr)):
        smallest = Smallest_element(arr) # find the smallest Array and adds to an new array
        New_arr.append(arr.pop(smallest))
    return New_arr

print(Smallest_element(['beatriz','Arthur','Aabrão']))