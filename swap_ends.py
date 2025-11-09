def swap_ends(L, k):
    
    if k <= 0 or len(L) == 0 or k > len(L) / 2:
        return (L.copy(), 0)
    
    first_k_values = L[:k]
    last_k_values = L[-k:]
    middle_values = L[k:-k]
    
    NEW_list = []
    NEW_list.extend(last_k_values)
    NEW_list.extend(middle_values)
    NEW_list.extend(first_k_values)
    
    return(NEW_list, k)

#%%
##Little explanation of what is occuring:
    
## lines 3-4 return a copy of L and 0 swaps based on the constraints

## we define the first and last k values of the list L and the remaining
## "middle values"

## we then rearrange these values in a new list such that the first and 
##last have been swapped and the middle values remain the same 