

def checkInterval(start, end):

    invalids = 0 # Count number of invalid IDs
    wait = 0
    for number in range(start,end+1):

        print(number)
        # Condition 1: Lenght of number is even
        if len(str(number)) % 2 != 0 or str(number)[:(len(str(number))//2)] != str(number)[len(str(number))//2:] or str(number)[0] == 0:
            wait += wait
        else:
            invalids += 1 # All conditions met, therefor number is invalid
            print(4)
    return invalids


print(checkInterval(11,12))
