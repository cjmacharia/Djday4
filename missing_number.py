def find_missing(first, second): #define the function with two parameters 
    getMissing = []             #initialize an empty array 
    for num in first:             #a loop through the numbers in first  
        if num not in second:       #condition
            getMissing.append(num) #if it satisfies add the num into the array
    for num in second:                     #condition
        if num not in first:
            getMissing.append(num)

    if len(getMissing) > 0:    # condition for the length of the array
                                            
        if len(getMissing) == 1: 
            return getMissing[0]
        else:
            return getMissing
    else:
        return 0  

print(find_missing([5, 4, 1], [5, 4, 1,90,6]))        #test