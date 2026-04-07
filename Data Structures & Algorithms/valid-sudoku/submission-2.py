class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range (0,9):
            rmap = {}
            cmap = {}
            for j in range (0,9):
                if board[i][j] != ".":
                    if board[i][j] in rmap:
                        print("check1")
                        return False
                    else:
                        rmap[board[i][j]] = 1
                if board[j][i] != '.':
                    if board[j][i] in cmap: 
                        print("check2")
                        return False
                    else: 
                        cmap[board[j][i]] = 1
        
        for l in range (0,3):
            for i in range (0,3): 
                sqmap = {}
                for k in range (0,3):
                    for j in range (0,3):
                        if board[j+3*i][k+3*l] != '.':
                            if board[j+3*i][k+3*l] in sqmap:
                                print (board[j+3*i][k+3*l])
                                print("check3")
                                return False
                            else:
                                sqmap[board[j+3*i][k+3*l]] = 1
        return True
