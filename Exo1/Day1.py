

#-------------------------------------------------
# Advent of Code 2025
# Day 1: Combination lock
#-------------------------------------------------

from collections import Counter 

# For Part 1
# We start by defining a simple fucntion to analyse the dial
def turnDial(command, dial):
    if command[0] == 'R': # Check if we add or substract
        # We add the following to the dial
        dial = dial + int(command[1:])
    else:
        # We substract from the dial
        dial = dial - int(command[1:])
    return  (dial % 100) # We return the value of the dial

# For Part 2
def checkZero(command, dial):
    zeros = int(int(command[1:])/100)
    if int(command[1:]) % 100 == 0 or dial == 0:
        return zeros
    
    if command[0] == 'R': # We know we've added to dial
        if dial > turnDial(command, dial) or turnDial(command, dial) == 0: # We passed zero another time
            zeros = zeros + 1        
    else:
        if dial < turnDial(command, dial) or turnDial(command, dial) == 0: # We passed zero another time
            zeros = zeros + 1        
    return zeros

# We define a main that opens a file and counts the most common dial
def main():

#-----------------------------------------------------------
# Part 1 Counting most frequent number
#-----------------------------------------------------------
    f = open("Day1.txt") # We open the document containing the commands
    numbers = [50] # We initialise a list to add the results of the commands

    # We check every line from the file and use turnDial
    for command in f.readlines():
        # We calculate the new number using the last value
        numbers.append(turnDial(command, numbers[len(numbers)-1]))
    del numbers[0] # We delete the 50 that we initialised
    
    # Numbers now contain all the results from all the commands
    # All we need to do now is to find the most common number
    number, freq = Counter(numbers).most_common(1)[0] # Most frequent number
    print(f"most the most common number is {number} occuring {freq} times")

    f.close() # We close the document to reset it
    
#-----------------------------------------------------------
# Part 2 Counting amount of zeros
#-----------------------------------------------------------
    f = open("Day1.txt") # We reopen the documents so that we can loop from the top again
    numbers = [50] # Reinitialisation of numbers to keep same naming scheme
    zeros = 0
    # We check every line in the file for the commands
    for command in f.readlines():
        zeros = zeros + checkZero(command, numbers[len(numbers)-1]) # Adding zeros from this iteration
        numbers.append(turnDial(command, numbers[len(numbers)-1])) # Calculating next dial
    print(f"the amount of zeros passed is {zeros}")

# We call on our function
main()
