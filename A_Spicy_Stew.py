testCases = int(input())

for i in range(testCases):
    chilliNum = int(input())
    chilliSpiciness = list(map(int, input().split()))
    
    if len(chilliSpiciness) != len(set(chilliSpiciness)): # Check for duplicates, True if present
        print("YES")
    else:
        print("NO")

