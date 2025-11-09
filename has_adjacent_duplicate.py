def has_adjacent_duplicate(L):
    
    for i in range(len(L) - 1):
        if L[i] == L[i + 1]:
            return True
    return False

#%%
## Little explanation of what is occuring:

## we define a list
## then with this list we make this iterative function that for every value 
## in said list, we check if the next value is equal to it. 
## this occurs for every value except for the last (hence L -1 for range)
## then for every two that equal eachother we return true, this runs for every 
## value in the list
## if true does not occur, it returns false. 
        
