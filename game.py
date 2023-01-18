from math import inf
from copy import deepcopy
class Game:

    def __init__(self, state, player_side):
        self.state = state
        self.player_side = player_side


    def game_over(self):
        # game is over when all foses of one player is empty
        # the oppossite player takes all his grains and puts them in his magazine

        # check if game is over
        
        for i in (1, 2):
            game_over = (1, i)
            for x in self.state.dict[i]:
                if self.state.board[x] != 0:
                    game_over = (0, i)
                    break
            if(game_over[0] == 1):
                break
        
        if game_over[0] == 1:
            # takes all the grains from the other player fosses and puts it in the magazine
            player = 1 if game_over[1] == 2 else 1
            for x in self.state.dict[player]:
                self.state.board[str(player)] += self.state.board[x]
                self.state.board[x] = 0
            
            return True
        
        else:
            return False 

    def find_winner(self):
        # check which player wins
        return 1 if self.state.board['1'] > self.state.board['2'] else 2

    def evaluate(self):
        # TODO: make a a better evaluation function
        weights = [1, 0.96, 0.33]
        return self.h_4() * weights[0] + self.h_7() * weights[1] + self.h_8() * weights[2]






    def h_4(self):
        possible_moves = self.state.possible_moves(self.player_side)
        best = 0
        for i in possible_moves:
            temp = self.state.do_move_test(i, self.player_side)
            if temp > best:
                best = temp
        return best

    def h_7(self):
        count = 6
        for i in self.state.dict[self.player_side]:
            if self.state.board[i] == count:
                return 2
            count -= 1
        return 0

    def h_8(self):
        computer_side = 1 if self.player_side == 2 else 2
        return self.state.board[str(computer_side)] - self.state.board[str(self.player_side)]


        

        





    @staticmethod
    def alpha_beta_pruning(game, player, depth, alpha, beta):
        other_player = 1 if player==2 else 2
        if game.game_over() or depth == 1:
            bestValue = game.evaluate()
            bestPit = None
            return bestValue, bestPit

        bestValue = +inf if player==game.player_side else -inf
        bestPit = None

        for pit in game.state.possible_moves(player):

            child_game = deepcopy(game)
            next_player = child_game.state.do_move(pit, player)
            value, _ = Game.alpha_beta_pruning(child_game, other_player if next_player != player else player, depth-1, alpha, beta)
            if player == game.player_side:
                # human MIN PLAYER
                if value < bestValue:
                    bestValue = value
                    bestPit = pit

                beta = min(beta, bestValue)
    
                # Alpha Beta Pruning
                if beta <= alpha:
                    break

            else:
                # computer MAX PLAYER
                if value > bestValue:
                    bestValue = value
                    bestPit = pit
                    
                alpha = max(alpha, bestValue)
    
                # Alpha Beta Pruning
                if beta <= alpha:
                    break

        return bestValue, bestPit
        

        


