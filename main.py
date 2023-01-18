from play import Play
from game import Game
from mancala_board import MancalaBoard
from gui import GameUI




def main():
    # main program lunch
    

    play = Play(Game(MancalaBoard(), 1))
    gameui = GameUI(play)
    
    play.human_turn()







if __name__ == "__main__":
    main()