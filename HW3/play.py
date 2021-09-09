import game
import gameGUI

board=game.game()
game.create(board)
print("Initial Game")
game.printState(board)

gameGUI.set_screen("Start Screen")
goesFirst = -1
while(goesFirst == -1):
    goesFirst = gameGUI.button_click()

#game.decideWhoIsFirst(board)
game.decideWhoIsFirst(board,goesFirst)

gameGUI.set_screen("Game Screen")

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
            gameGUI.drop_sound()
    else:
        board=game.inputComputer(board)
        winner = game.printState(board)
        gameGUI.draw_board(board.board)
        gameGUI.drop_sound()

    if game.isFinished(board):
        gameGUI.print_gameover_msg(winner)
        gameGUI.sleep_screen(15)

print("Game Over:")