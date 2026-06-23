stop = False

for i in range(3):

    for j in range(3):
        print(i, j)

        if i == 1 and j == 1:
            stop = True
            break

    if stop:
        print("In STOP", i, j)
        break

print("Loop Stopped")