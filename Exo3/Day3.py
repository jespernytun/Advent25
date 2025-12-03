

#-----------------------------------------------
# Advent of Code
# Day 3: Largest number
#-----------------------------------------------


def findLargest(chain):

    index = 0
    first = 0
    for i in range(len(chain[:-1])):
        digit = int(chain[i])
        if digit > first:
            first = digit
            index = i

    second = 0
    chain = chain[index+1:]
    for i in range(len(chain)):
        digit = int(chain[i])
        if digit > second:
            second = digit

    number = str(first) + str(second)
    return int(number)
        
def main():

    tot = 0
    with open("Day3.txt") as f:
        for chain in f.readlines():
            chain = chain.strip()
            tot += findLargest(chain)
            
    print(f"The sum of the largest numbers is {tot}")

main()


