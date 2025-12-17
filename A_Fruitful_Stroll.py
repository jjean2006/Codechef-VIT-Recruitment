testCases = int(input())

for tc in range(testCases):
    n = int(input())
    trees = list(map(int, input().split()))

    numFruitsMax = 0

    left = 0
    right = 0
    count = {}

    for right in range(n):
        fruit = trees[right]
        count[fruit] = count.get(fruit, 0) + 1 # Maintain count of fruits

        while len(count) > 2: # If more than 2 fruits present, shrink window from left
            left_fruit = trees[left]
            count[left_fruit] -= 1
            if count[left_fruit] == 0:
                del count[left_fruit]
            left+=1

        numFruitsMax = max(numFruitsMax, right - left + 1) # Update max
    print(numFruitsMax)

