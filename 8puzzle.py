import random as r

goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]

def moveUp(board):
    idx = board.index(0)
    if idx >= 3:
        board[idx], board[idx - 3] = board[idx - 3], board[idx]
    return board

def moveDown(board):
    idx = board.index(0)
    if idx <= 5:
        board[idx], board[idx + 3] = board[idx + 3], board[idx]
    return board

def moveLeft(board):
    idx = board.index(0)
    if idx % 3 != 0:
        board[idx], board[idx - 1] = board[idx - 1], board[idx]
    return board

def moveRight(board):
    idx = board.index(0)
    if idx % 3 != 2:
        board[idx], board[idx + 1] = board[idx + 1], board[idx]
    return board

def show(board):
    print(board[0], board[1], board[2])
    print(board[3], board[4], board[5])
    print(board[6], board[7], board[8])

def huristic(board):
    count = 0    
    for number in range(1, 9):
        t = board.index(number)
        p = goal.index(number)
        count += calculate(t, p)
    return count

def calculate(num1, num2):
    row = abs((num1 % 3) - (num2 % 3))
    col = abs((num1 // 3) - (num2 // 3))
    return row + col
    
def isMove(board, function):
    temp = board.copy()
    if board == function(temp):
        return False
    return True

def moveAuto(board):
    if board == goal:
        return board
        
    best = float('inf')
    bestFunction = []
    functionList = [moveUp, moveDown, moveLeft, moveRight]
    for function in functionList:
        if isMove(board, function):
            temp = board.copy()
            temp = function(temp)
            if best > huristic(temp):
                best = huristic(temp)
                bestFunction = []
                bestFunction.append(function)
    
    return bestFunction[0](board)

def moveRandom(board):
    functionList = [moveUp, moveDown, moveLeft, moveRight]
    for function in functionList:
        if not isMove(board, function):
            functionList.remove(function)
    rd = r.randrange(0, len(functionList))
    
    return functionList[rd](board)
           
def main():
    puzzle_board = [1, 2, 3, 4, 5, 6, 7, 8, 0]
         
    while True:
        show(puzzle_board)
        user_input = int(input("1. Move / 2. Huristic / 3. Shuffle : "))
        if user_input == 1:
            user_input == int(input("1. Up / 2. Down / 3. Left / 4. Right : "))
            if user_input == 1:
                puzzle_board = moveUp(puzzle_board)
        
            elif user_input == 2:
                puzzle_board = moveDown(puzzle_board)
                
            elif user_input == 3:
                puzzle_board = moveLeft(puzzle_board)
                
            elif user_input == 4:
                puzzle_board = moveRight(puzzle_board) 
        
        elif user_input == 2:
            cnt = 0
            while True:
                puzzle_board = moveAuto(puzzle_board)
                cnt += 1
                
                if puzzle_board == goal:
                    show(puzzle_board)
                    print("Solved : %d movement take" % cnt)
                    break
                
                if cnt == 1000:
                    show(puzzle_board)
                    print("Can't Solve")
                    break

        elif user_input == 3:
            user_input = int(input("How many times? : "))
            for i in range(user_input):
                puzzle_board = moveRandom(puzzle_board)



if __name__ == "__main__":
    main()
