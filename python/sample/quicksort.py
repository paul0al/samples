import random

# python does not have pre/post increment operators

def sort(data): 
    """In place quick sort."""
    if(isinstance(data, list)):
        __sort(data, 0, len(data) - 1)
    else:
        raise TypeError("accepts list data types only")

def __sort(data, start_index, end_index):
    if(start_index < end_index):
        pivot_index = random.randint(start_index, end_index)
        pivot = data[pivot_index]
        
        __swap(data, pivot_index, end_index)
        write_index = start_index
        
        for i in range(start_index, end_index):
            if(data[i] < pivot): 
                __swap(data, i, write_index)
                write_index += 1
        
        __swap(data, end_index, write_index)
        
        __sort(data, start_index, write_index - 1)
        __sort(data, write_index + 1, end_index)

def __swap(data, from_index, to_index):
    temp = data[to_index]
    data[to_index] = data[from_index]
    data[from_index] = temp
    
    # would this work: data[to_index], data[from_index] = data[from_index], temp
