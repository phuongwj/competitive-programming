n = int(input())
lowest = 0
highest = 2e5
for _ in range(n):
    low, high = map(int, input().split())

    if low >= lowest:
        lowest = low

    if high <= highest:
        highest = high

if lowest > highest:
    print("bad news")
else:
    diffIntegers = highest - lowest + 1
    print(diffIntegers, lowest)