#Problem:
#Given a list of integers, write a Python function to find the two numbers that sum up to a given target value. Return the indices of the two numbers as a tuple.

#Example:
#Input:
#numbers = [2, 7, 11, 15, 3, 6]
#target = 9
#Output:
#(0, 1)

def two_sum(numbers, target):
    num_dict = {}
    for i, num in enumerate(numbers):
        complement = target - num
        if complement in num_dict:
            return(num_dict[complement],i) 
        num_dict[num] = i
    return None
number = [2,7,11,15,3,6]
target = 9
result = two_sum(number,target)
print(result)