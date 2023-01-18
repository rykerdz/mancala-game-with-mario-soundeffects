from copy import deepcopy
class MancalaBoard:

    def __init__(self, board={}):
        self.board = MancalaBoard.setup_board(board) if board=={} else board
        self.opposed_dict = MancalaBoard.setup_opposed_dict()
        self.next_dict = {'A': 'B', 'B': 'C', 'C': 'D', 'D': 'E', 'E': 'F', 'F': '1', '1': 'L', 'L': 'K', 'K': 'J', 'J': 'I', 'I': 'H', 'H': 'G', 'G': '2', '2': 'A'}
        self.dict = {1: ['A', 'B', 'C', 'D', 'E', 'F'], 2: ['G', 'H', 'I', 'J', 'K', 'L']}

    def setup_board(board):
        for x in range(0, 12):
            board[chr(65+x)] = 4 # 4 is the number of grains in the opening
        board['1'] = 0
        board['2'] = 0
        return board
    

    def possible_moves(self, player):
        possible_moves = []
        for x in self.dict[player]:
            if self.board[x] != 0:
                possible_moves.append(x)
        return possible_moves
    
    def setup_opposed_dict():
        opposed_dict = {}
        for x in range(0, 6):
            opposed_dict[chr(65+x)] = chr(65+6+x) # chr of 65 = A
            opposed_dict[chr(65+6+x)] = chr(65+x)
        return opposed_dict
    
    def do_move(self, grain, player):
        next = grain
        other_player = 1 if player==2 else 2
        iterer = self.board[grain]
        self.board[grain] = 0
        while(iterer!=0):
            next = self.next_dict[next]
            if(next!=str(other_player)):
                self.board[next] += 1
                iterer -= 1

        if(next == str(player)): # last foss is player magazine -> player plays again
            return player # play again
        
        if(self.board[next]==1 and next in self.dict[player]): # foss vide , player takes whats in his opposite
            x = self.board[next] # takes whats in his foss
            self.board[next] = 0 # set to zero
            x += self.board[self.opposed_dict[next]] # and takes whats in his opposite foss
            self.board[self.opposed_dict[next]] = 0 # set his opposite foss to zero

            self.board[str(player)] += x # add all that to the player magasine
        return other_player # give hand to the other player

    

    def do_move_test(self, grain, player):
        next = grain
        count = 0
        other_player = 1 if player==2 else 2
        iterer = self.board[grain]
        self.board[grain] = 0
        while(iterer!=0):
            next = self.next_dict[next]
            if(next == str(player)):
                count += 1
            if (next != str(other_player)):
                iterer -= 1
        
        if(self.board[next] == 0 and next in self.dict[player]): # foss vide , player takes whats in his opposite
            count = self.board[next] # takes whats in his foss
            count += self.board[self.opposed_dict[next]] # and takes whats in his opposite foss
        
        return count
        





    








