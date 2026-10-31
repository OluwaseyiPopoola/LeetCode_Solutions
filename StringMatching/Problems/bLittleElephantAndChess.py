alternating = True

for _ in range(8):


    row = input()

    for i in range(1, len(row)):
        alternating = alternating and (row[i - 1] != row[i])


if alternating:
    print("YES")

else:
    print("NO")


