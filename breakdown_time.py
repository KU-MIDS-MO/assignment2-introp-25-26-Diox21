def breakdown_time(seconds):
    if type(seconds) != int or seconds < 0:
        return -1
    if seconds == 0:
        return {}
    
    h = 0
    while seconds >= 3600:
        h += 1
        seconds -= 3600
        
        
    m = 0
    while seconds >= 60:
        m += 1
        seconds -= 60
        
    s = seconds
    
    return {3600: h, 60: m, 1: s}

#%%
## Little explanation of what is occurring here:

## we first define a variable for our value of seconds
## we then run a non integer and less than 0 check
## we then run a 0 check

## we then start with h = 0 and for however multiples of 3600 there are in 
## the value of seconds we add a value to h 

## we do the same thing for minutes with multiples of 60

## the remainder after seconds is less than 60 is noted as the value of s

## we then arrange all of these to be returned as above
    