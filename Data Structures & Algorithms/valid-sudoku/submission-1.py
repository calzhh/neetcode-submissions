import copy
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # horizontal to vertical
        horizontalToVertical = [[] for i in range(0,9)]
        for i in range(len(board)):
            for j in range(0,9):
                horizontalToVertical[i].append(board[j][i])
        
        im_going_to_mutate_this_board_normal = copy.deepcopy(board)
        im_going_to_mutate_this_board_90 = copy.deepcopy(horizontalToVertical)

        for row in im_going_to_mutate_this_board_normal:
            row = [x for x in row if x != "."]
            if len(row) != len(set(row)):
                return False

        for row in im_going_to_mutate_this_board_90:
            row = [x for x in row if x != "."]
            if len(row) != len(set(row)):
                return False
        for row in range(0,9,3):
            for col in range(0,9,3):
                boxseen = set()
                boxlist = []
                for i in range(row,row+3):
                    for j in range(col,col+3):
                        if board[i][j] != '.':
                            boxseen.add(board[i][j])
                            boxlist.append(board[i][j])
                if len(boxseen) != len(boxlist):
                    print(boxseen, boxlist)
                    return False
        return True