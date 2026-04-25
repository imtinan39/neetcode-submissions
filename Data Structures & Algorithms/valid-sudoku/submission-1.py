class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            dic={}
            for j in range(9):
                if board[i][j] not in dic:
                    dic[board[i][j]]=dic.get(board[i][j],0)+1
                elif board[i][j] in dic and board[i][j]!=".":
                    return False
            for i in range(9):
                dic={}
                for j in range(9):
                    if board[j][i] not in dic:
                        dic[board[j][i]]=dic.get(board[j][i],0)+1
                    elif board[j][i] in dic and board[j][i]!=".":
                        return False
            for i in range(9):

                if i%3==0:
                    dic={}
                for j in range(0,3):
                    if board[i][j] not in dic:
                        dic[board[i][j]]=dic.get(board[i][j],0)+1
                    elif board[i][j] in dic and board[i][j]!=".":
                        return False
            for i in range(9):

                if i%3==0:
                    dic={}
                for j in range(3,6):
                    if board[i][j] not in dic:
                        dic[board[i][j]]=dic.get(board[i][j],0)+1
                    elif board[i][j] in dic and board[i][j]!=".":
                        return False
            for i in range(9):

                if i%3==0:
                    dic={}
                for j in range(6,9):
                    if board[i][j] not in dic:
                        dic[board[i][j]]=dic.get(board[i][j],0)+1
                    elif board[i][j] in dic and board[i][j]!=".":
                        return False
        return True
                    

            
        