def minJumps(arr, n):
    # get first element, def initial index
    position = 0
    minJumps = 0

    while (True):
        currentJump = arr[position]
        minJumps += 1

        if currentJump+position >= n-1:
            return minJumps

        nextPos = 0
        maxJump = 0

        for i in range(position+1, position+currentJump+1):
            jumpPlusIndex = arr[i]+i
            if jumpPlusIndex > maxJump:
                nextPos = i
                maxJump = jumpPlusIndex

        position = nextPos

        if maxJump == 0:
            return -1


def main():
    N = 6
    arr = [1, 4, 3, 2, 6, 7]

    print(minJumps(arr, N))


if __name__ == '__main__':
    main()
