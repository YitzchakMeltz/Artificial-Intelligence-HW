import game
import gameGUI

board=game.game()
game.create(board)
print("Initial Game")
game.printState(board)

game.decideWhoIsFirst(board)

while not game.isFinished(board):

    col = gameGUI.handle_events()
    winner = -1 

    if col != -1:
        print("continue game")
    
    if game.isHumTurn(board):
        if col != -1:
            game.inputMove(board,col)
            winner = game.printState(board)
            gameGUI.draw_board(board.board)
    else:
        board=game.inputComputer(board)
        winner = game.printState(board)
        gameGUI.draw_board(board.board)

    if game.isFinished(board):
        gameGUI.print_gameover_msg(winner)
        gameGUI.sleep_screen(15)

print("Game Over:")