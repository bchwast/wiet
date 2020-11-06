import random
if __name__ == "__main__":
    n = int(input("n = ")) # kolumny
    matrix = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            matrix[i][j] = random.randint(0,256)
    print(matrix)
    for i in range(n):
        print(matrix[i])

    while True:
        command = input("> ")
        if command == "flip horizontal":
            matrix = matrix[::-1]
        elif command == "flip vertical":
            for i in range(n):
                matrix[i] = matrix[i][::-1]
        elif command == "rotate left":
            for x in range(n//2):
                for y in range(x,n-x-1):
                    temp = matrix[x][y]
                    matrix[x][y] = matrix[y][n-1-x]
                    matrix[y][n-1-x] = matrix[n-1-x][n-1-y]
                    matrix[n-1-x][n-1-y] = matrix[n-1-y][x]
                    matrix[n-1-y][x] = temp
        elif command == "rotate right":
            for x in range(n//2):
                for y in range(x,n-x-1):
                    temp = matrix[x][y]
                    matrix[x][y] = matrix[n-1-y][x]
                    matrix[n-1-y][x] = matrix[n-1-x][n-1-y]
                    matrix[n-1-x][n-1-y] = matrix[y][n-1-x]
                    matrix[y][n-1-x] = temp
        elif command == "reverse values":
            for i in range(n):
                for j in range(n):
                    matrix[i][j] = 255 - matrix[i][j]
        elif command == "done":
            break
    for i in range(n):
        print(matrix[i])
