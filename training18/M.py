N, M, L = map(int, input().split())

s = []
for i in range(N):
    row = list(map(int, input().split()))
    s.append(row)

pos = [0] * N # to store sheep positions
count = [0] * 12 # to store the occurrences of the instructions
active = [True] * N

for _ in range(M):
    instruction = int(input())

    if instruction != 12:
        count[instruction] += 1
    else:
        right = [] # indices of sheep running right
        caughtRight = -1 # smallest-index catchable right
        caughtLeft = -1 # smallest-index catchable left

        for i in range(N):
            if not active[i]:
                continue

            # 1. move the sheep
            total = 0
            for X in range(1, 12):
                total += count[X] * X * s[i][X-1]
            pos[i] += min(L, pos[i] + total)

            # 2. direction and D
            if pos[i] >= L/2:
                D = L - pos[i]
                right.append(i)

                if L < 4*D and caughtRight == -1:
                    caughtRight = i
            else:
                D = pos[i]
                if L < 4 * D and caughtLeft == -1:
                    caughtLeft = i

        # 3. Who does the fox catch? (rights are prioritized)
        if caughtRight != -1:
            caught = caughtRight
        else:
            caught = caughtLeft # -1 if nobody

        # 4. sheep that reached the right side safely (everyone
        # running right except the caught one)
        safe = []
        for i in right:
            if i != caught:
                safe.append(i + 1) # +1 because sheep are numbered from 1

        # print the safe sheep
        if len(safe) == 0:
            print("None")
        else:
            print(" ".join(map(str, safe)))

        # print the caught sheep
        if caught == -1:
            print("None")
        else:
            print(caught + 1)

        # 5. update state
        for i in right:
            active[i] = False # reached the right side (or caught)
        if caught != -1:
            active[caught] = False
        for i in range(N):
            if active[i]:
                pos[i] = 0 # left runners restart at 0

        count = [0] * 12