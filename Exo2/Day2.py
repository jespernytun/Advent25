
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
    tot = 0 # Count number of invalid IDs
    for number in range(start,end+1):
        # Condition 1: Lenght of number is even
        if len(str(number)) % 2 != 0:
            continue
        # Condition 2: Slice one equal to slice two
        if str(number)[:(len(str(number))//2)] != str(number)[len(str(number))//2:]:
            continue
        # Condition 3: Number does not start with a zero
        if str(number)[0]== 0:
            continue
        else:
            tot += int(str(number)) # All conditions met, therefor number is invalid
            
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
    print(f"The sum  of invalids in this document is {invalids}")

    
#----------------------------------------------------------------------------
# Part 2: Generalized, multiple cuts
#----------------------------------------------------------------------------

    # We reinitialise all our values
    starts, ends = getIntervals()
    invalids = 0


main()
