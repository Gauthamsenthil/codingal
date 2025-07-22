#Implementing of two player stic-tac-toe game in python.
'''we will make the board using dictionary.in which keys will be the location(i.e.: top-left,mid-right etc.) and initially it's values wiill be empty space and then after every move.we will change the value according to player's choice of move'''
theBoard = {'7':' ','8':' ','9':' ',
            '4':' ','5':' ','6':' ',
            '1':' ','2':' ','3':' '}
board_keys = []
for key in theBoard:
    board_keys.append(key)
'''we will have to print the updated board after very move in the game and
thus we wll make a function in which we'll define the printBoard function
so that it can easily print the board everytime by calling this function'''

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

#now we'll write the main function which has all the gameplay functionality
def game():
    turn = 'X'
    count = 0

    for i in range(10):
        printBoard(theBoard)
        print("It's your turn"+ turn +".Move to which place?")
    
        move = input()

    if theBoard[move] == ' ':
        theBoard[move] = turn
        count += 1
    else:
        print("that place is already filled.\nMove to which place?")
        continue

#now we will check if player X or O has won, for every move after 5 moves.
    if count >=5:
        if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': #across the top
            printBoard(theBoard)
            print("\n GAME OVER \n")
            print("****" +turn+ "won. ****")
            break
        elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': #across the top
            printBoard(theBoard)
            print("\n GAME OVER \n")
            print("****" +turn+ "won. ****")
            break
        elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': #across the top
            printBoard(theBoard)
            print("\n GAME OVER \n")
            print("****" +turn+ "won. ****")
            break
        elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': #across the top
            printBoard(theBoard)
            print("\n GAME OVER \n")
            print("****" +turn+ "won. ****")
            break
        elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': #across the top
            printBoard(theBoard)
            print("\n GAME OVER \n")
            print("****" +turn+ "won. ****")
            break
        elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': #across the top
            printBoard(theBoard)
            print("\n GAME OVER \n")
            print("****" +turn+ "won. ****")
            break
        elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': #across the top
            printBoard(theBoard)
            print("\n GAME OVER \n")
            print("****" +turn+ "won. ****")
            break
        elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': #across the top
            printBoard(theBoard)
            print("\n GAME OVER \n")
            print("****" +turn+ "won. ****")
            break
        #if neither X nor 0 wins and the board is full.we'll declare the result as 'tie'
        if count == 9:
            print("\nGAME OVER.\n")
            print("it's a tie")
        #now we have to change the player after every move
        if turn == 'X':
            turn = '0'
        else:
            turn = 'X'

        #now we will ask if player wants to restart the game or not.
    restart = input("do you want to play again?(Y/N)")
    if restart == 'Y' or restart == 'y':
        for key in board_keys:
            theBoard[key] = " "

        game()
if __name__ == "__main__":
    game()