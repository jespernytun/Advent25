#------------------------------------------------
# Adventofcode 2025
# Day4: Forklifts
# Autor: Jesper Nytun
#------------------------------------------------


# I want to store all the lines in the document in a matrix
def createMatrix():
    matrix = []

    with open("Day4.txt") as f:
        for chain in f.readlines():
            chain = chain.strip()
            stack = []
            for i in range(len(chain)):
                stack.append(chain[i])
            matrix.append(stack)

    return matrix

# We search the warehouse for removable objects
def searchWarehouse(Matrix):
    # Total accessible rolls
    rolls = 0
    rows = len(Matrix)
    cols = len(Matrix[0])
    
    # Directions to search, as in OthelloSDL3
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
    removable = []
    
    # We serach every pallet that isn't on the edges to begin with
    for r in range(rows):
        for c in range(cols):
            if Matrix[r][c] != '@':
                continue
            surround = 0
            for dr, dc in directions:
                # Checking directions around
                newr = r + dr
                newc = c + dc
                # Verify coordinates
                if 0 <= newr < rows and 0 <= newc < cols:
                    if Matrix[newr][newc] == '@':
                        surround += 1
            if surround < 4:
                rolls += 1
                removable.append((r, c))
                
    return rolls, removable

def emptyWarehouse(Matrix):
    tot = 0
    empty = False
    rolls, removable = searchWarehouse(Matrix) # We search coordinates for all removable objects
    
    while not empty: # While it's not empty (as in possible to remove more) we loop

        tot += rolls
        # We iterate to remove these objects
        for square in removable:
            Matrix[square[0]][square[1]] = '.'

        # We check again if there are removable objects
        rolls, removable = searchWarehouse(Matrix)
        if not removable: # If list returns empty, we stop iterating, no more objects to remove
            empty = True

    return tot

def main():

    warehouse = createMatrix()
    print(f"Number of accesible rolls on first iteration {searchWarehouse(warehouse)[0]}")
    print(f"Number of accesible rolls in {emptyWarehouse(warehouse)}")

main()
