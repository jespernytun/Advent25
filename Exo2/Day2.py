
#-------------------------------------------------------------
# Advent of Code
# Day 2: ProductIDs
#-------------------------------------------------------------

# First thoughts, this really resembles a project I did this summer
# https://www.github.com/jespernytun/pricelist_converter
# I will therefore be using regex to solve this problem, because it's familiar

import re

# I'll start by making a function that can read the following input
def getIntervals():
    f = open("Day2.txt") # We open todays file
    intervals = re.split(",", str(f.read())) # We split all the intervals
    
    starts = [] # Array to store inverval starts
    ends = [] # Array to store inverval ends    
    for i in range(len(intervals)):
        starts.append(int(re.split("-", intervals[i])[0]))
        ends.append(int(re.split("-", intervals[i])[1]))

    return starts, ends

# We make a function that counts illegal IDs in an interval
# This is works for the part 1
def checkInterval(start, end):
    tot = 0 # Initialize total
    for number in range(start,end+1):
        # Condition 1: Lenght of number is even
        if len(str(number)) % 2 != 0:
            continue
        # Condition 2: Slice one equal to slice two
        if str(number)[:(len(str(number))//2)] != str(number)[len(str(number))//2:]:
            continue
        # Condition 3: Number does not start with a zero
        if str(number)[0] == 0:
            continue
        else:
            tot += int(str(number)) # All conditions met, therefor number is invalid
        
    return tot

# This is a function that finds different possible tranches of a number
def findCuts(number):
    # We find the different kinds of tranching that is possible for a number
    # Eg, 1111 can be cut into 1¦¦1¦1¦1 or 11¦11
    sizes = [] # We would in that case store 1 and 2
    for n in range(1, (len(str(number))//2)+1):
        if len(str(number)) % n == 0: # We use mod n to caluculate different possible sizes
            sizes.append(n)
            
    for s in sizes:
        partition = [] # This is where we'll save our slices
        valid = False   # We assume the number is invalid
        
        # We split the string into equal parts of size s
        for i in range(0, len(str(number)), s):
            partition.append(str(number)[i:i+s])
        
        # We test if all sizes are equal
        n = 1 # Iteration counter
        while not valid and n < len(str(number))//s: # while not all values checked -> loop
            if partition[n] != partition[n-1]: # If two partitionsun equal we know number is valid
                valid = True  # So we skip to check next iteration
            n += 1
            
            if valid == False and n == len(str(number))//s: # We know we found at lease one invalid soulution
                return number # Therefore returning is safe
            
    return 0 # Number has been tested, we return 0
            
# Same as checkinterval but generalized for part 2   
def checkIntervalGeneralized(start, end):
    tot = 0 # Count number of invalid IDs

    for number in range(start, end+1):
        #Condition 1: Number does not start with a zero
        if str(number)[0] == 0:
            continue
        
        tot+=findCuts(number)
        
    return tot

def main():

#----------------------------------------------------------------------------
# Part 1: Edge case, cut down the middle
#----------------------------------------------------------------------------
    
    # We use get intervals to get out intervals for check intervals
    starts, ends = getIntervals()
    invalids = 0
    
    for i in range(len(starts)):
        invalids +=  checkInterval(starts[i], ends[i])
    print(f"The sum  of simple invalids in this document is {invalids}")

    
#----------------------------------------------------------------------------
# Part 2: Generalized, multiple cuts
#----------------------------------------------------------------------------

    invalids = 0 # Reset invalids
    for i in range(len(starts)):
        invalids +=  checkIntervalGeneralized(starts[i], ends[i])        
    print(f"The sum  of all generalized invalids in this document is {invalids}")

main()
