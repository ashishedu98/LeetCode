class Solution(object):

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rowEntries =''
        colEntries = ''
        gridEntries = ''
        for row in range(9):
            for col in range(9):
                if board[row][col]!= '.':
                    tempRow = ',r'+ str(row)+'n'+str(board[row][col])
                    tempCol = ',c'+str(col)+'n'+str(board[row][col])
                    tempGrid = ',g'+returnGrid(row,col)+'n'+str(board[row][col])
                    if tempRow in rowEntries or tempCol in colEntries or tempGrid in gridEntries:
                        return False
                    else:
                        rowEntries += tempRow
                        colEntries += tempCol
                        gridEntries += tempGrid

        return True
def returnGrid(row,col):
    if row<3:
        if col<3:
            return 'g1'
        elif col>2 and col<6:
            return 'g2'
        else:
            return 'g3'
    elif row>2 and row<6:
        if col<3:
            return 'g4'
        elif col>2 and col<6:
            return 'g5'
        else:
            return 'g6'
    else:
        if col<3:
            return 'g7'
        elif col>2 and col<6:
            return 'g8'
        else:
            return 'g9'

    
        