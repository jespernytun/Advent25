#-----------------------------------------------
# Advent of Code
# Day 3: Largest number
# Author jespernytun
#-----------------------------------------------


def findLargest(chain):

    # Here we're doing a loop to find the first occurence of the highest value (that isnt last)
    # Priciple of order of magnitude
    index = 0 
    first = 0
    for i in range(len(chain[:-1])):
        digit = int(chain[i])
        if digit > first: 
            first = digit
            index = i

    # We do the same but for the second value, but only from values that comes after the first one
    second = 0
    chain = chain[index+1:]
    for i in range(len(chain)):
        digit = int(chain[i])
        if digit > second:
            second = digit

    # We resturn the following number from our calculations
    number = str(first) + str(second)
    return int(number)

# This is for part two
def removeBattery(chain):
    
    k = len(chain) - 12  # We remove number such that only 12 remain
    tab = []

    # We search the chain and delete all numbers followed by a larger one
    # Search stops if it finds a number so far back we can't delete everthing in front of it
    for digit in chain:
        while k > 0 and tab and tab[-1] < digit:
            tab.pop()
            k -= 1 # One number removed
        tab.append(digit)
        
    # We haven't found enough numbers
    if k > 0:
        tab = tab[:-k] # We delete the least important ones

    return int("".join(tab)) # To avoid type errors


def main():

    tot = 0
    jot = 0
    with open("Day3.txt") as f:
        for chain in f.readlines():
            chain = chain.strip()
            tot += findLargest(chain)
            jot += removeBattery(chain)
            
    print(f"The sum of the largest numbers is {tot}")
    print(f"The sum of the largest numbers is {jot}")

main()


