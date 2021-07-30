import time
import os
import sys
from termcolor import colored
import art

print(colored("coded by ===> ", "green"), end="")
print(colored("Naser Rezayi", "blue"))
print(colored("github --> naserrezayi1998", "red"))
print()
print()
time.sleep(1)


def printProgressBar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█', printEnd="\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 *
                                                     (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=printEnd)
    if iteration == total:
        print()


items = list(range(0, 57))
l = len(items)

printProgressBar(0, l, prefix='Progress:', suffix='Complete', length=50)
for i, item in enumerate(items):
    # Do stuff...
    time.sleep(0.01)
    os.system("clear")
    print(colored("coded by ===> ", "green"), end="")
    print(colored("Naser Rezayi", "blue"))
    print(colored("github --> naserrezayi1998", "red"))
    print()
    print()
    print("|")
    print("|")
    print(" ---->")
    print(colored("    LOADING", "yellow"))
    # Update Progress Bar
    printProgressBar(i + 1, l, prefix=' ',
                     suffix='Complete\n', length=50)
print("       |")
print("       |")
print("        ---->")
print(colored("      STARTING THE GAME  ", "green"))
time.sleep(2)

board = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
empty = [0, 1, 2, 3, 4, 5, 6, 7, 8]


def display_board():
  print('     |     |      ')
  print('  ' + board[0]+'  |  '+board[1]+'  |  '+board[2])
  print('     |     |      ')
  print('------------------')
  print('     |     |      ')
  print('  ' + board[3]+'  |  '+board[4]+'  |  '+board[5])
  print('     |     |      ')
  print('------------------')
  print('     |     |      ')
  print('  ' + board[6]+'  |  '+board[7]+'  |  '+board[8])
  print('     |     |      ')


def player_input(player):
  player_symbol = ['X', 'O']
  correct_input = True

  position = int(input('player {playerNo} chance! Choose field to fill {symbol} '.format(
      playerNo=player + 1, symbol=player_symbol[player])))

  if board[position] == 'X' or board[position] == 'O':
    correct_input = False

  if not correct_input:
    print("Position already equipped")
    player_input(player)
  else:
    empty.remove(position)
    board[position] = player_symbol[player]
    return 1


def check_win():

  player_symbol = ['X', 'O']
  winning_positions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [
      0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

  for check in winning_positions:
    first_symbol = board[check[0]]
    if first_symbol != ' ':
      won = True
      for point in check:
        if board[point] != first_symbol:
          won = False
          break
      if won:
        if first_symbol == player_symbol[0]:
          print('player 1 won')
        else:
          print('player 2 won')
        break
    else:
      won = False

  if won:
    return 0
  else:
    return 1


def play():
  player = 0
  while empty and check_win():
    os.system("clear")
    display_board()
    player_input(player)
    player = int(not player)
  if not empty:
    print("NO WINNER!")


if __name__ == '__main__':
  play()
