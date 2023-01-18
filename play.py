from math import inf
from time import sleep
class Play:

    def __init__(self, game):
        self.game = game


    def human_turn(self, foss): # allows human to play
        next_player = self.game.state.do_move(foss, self.game.player_side)
        return next_player




    def computer_turn(self): # allows computer to play

        other_side = 1 if self.game.player_side == 2 else 2
        _, x = self.game.alpha_beta_pruning(self.game, other_side, 10, -inf, +inf) # evaluate with alpha beta pruning
        return x




    def show_board(self):
        board = self.game.state.board
        side = self.game.player_side
        other_side = 1 if side == 2 else 2
        print(" _ _ _ _ _ _ _ _ _  ")
        for x in self.game.state.dict[other_side]:
            print(" {}".format(x), end="")
        
        print("")

        for x in self.game.state.dict[other_side]:
            print(" {}".format(board[x]), end="")

        print("")
        
        print("{}               {} ".format(board[str(other_side)], board[str(side)]))

        for x in self.game.state.dict[side]:
            print(" {}".format(board[x]), end="")
        print("")
        for x in self.game.state.dict[side]:
            print(" {}".format(x), end="")
        print("")

        

        print(" _ _ _ _ _ _ _ _ _ _ ")


        




