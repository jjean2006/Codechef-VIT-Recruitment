testCases = int(input())

for i in range(testCases):
    singWord = input()
    plurWord = singWord[:-2] + "oi" # Remove last 2 characters and add “oi”
    print(plurWord)

