import random

def get_attack (turn, game_board_attack, game_board_user, diff):
  if turn == 1:
    move = user_move(game_board_attack)
  else:
    move = comp_move(game_board_user, diff)
  return move

def user_move(game_board_attack):
  size=len(game_board_attack)
  valid = False
  print("Your attacking board: ")
  display_board(game_board_attack)
  while not valid :
    attackcol = input('please enter column number of attack:')
    attackrow = input('please enter row number of attack:')
    if  attackcol.isdigit() and int(attackcol) < size and int(attackcol)>0 and attackrow.isdigit() and int(attackrow) < size and int(attackrow)>0 :
        move = [attackrow,attackcol]
        return move
    else:
      print ("please try again with integers between 1 and 9 for both inputs")

def hard_move(game_board_user):
  listofships = []
  listofsea = []
  for i in range(len(game_board_user)):
      for j in range(len(game_board_user)):
        if game_board_user[i][j]=="S":
          listofships.append([i, j])
        elif game_board_user[i][j] == "o":
          listofsea.append([i, j])
  decider = (random.randint(1,10))
  if decider >= 5 :
    return random.choice(listofships)
  else:
    return random.choice(listofsea)

def easy_move(game_board_user):
  attackrow=(random.randint(1,9))
  attackcol=(random.randint(1,9))
  move = [attackrow,attackcol]
  return move

def comp_move(game_board_user, diff):
  if diff == 'e':
    return easy_move(game_board_user)
  else:
    return hard_move(game_board_user)

def place_ship(col, row, length, orientation, board):
    if orientation == "v":
        for i in range(length):
            board[row+i][col] = "S"
    else:
        for x in range(length):
            board[row][col+x] = "S"
    return board

def comp_board(board):
    ships= [5,4,3,3,2]
    board1=create_board(len(board))

    board1 = place_ship(1, 1, ships[0], 'h', board1)
    board1 = place_ship(9, 3, ships[1], 'v', board1)
    board1 = place_ship(2, 2, ships[2], 'v', board1)
    board1 = place_ship(5, 4, ships[3], 'v', board1)
    board1 = place_ship(8, 2, ships[4], 'h', board1)

    return board1


def check_and_add_ship(board, length_ship):
    size=len(board)
    checked=False


    while not checked:
        empty=True
        done=False
        space=False
        col = False
        row = False
        orientation = False

        display_board(board)
        print ("Place the ship of length: " + str(length_ship))

        while not orientation:
            orientation = input('Please enter orientation (h,v) : ')
            if orientation != 'v' and orientation != 'h':
                orientation=False
                print ('Invalid orientation. Try entering v or h')

        while not col:
            col = input('Please enter column coordinate:')
            if not (col.isdigit() and int(col) <= size and int(col)>0):
                col=False
                print ('Invalid column. Try entering a number between 1 and ' + str(size))

        while not row:
            row = input('Please enter row coordinate:')
            if not (row.isdigit() and int(row) <= size and int(row)>0):
                row=False
                print ('Invalid row. Try entering a number between 1 and ' + str(size))

        p_row=int(row)
        p_col=int(col)

        row=int(row)
        col=int(col)

        if orientation=='v':
            end_ship=row+length_ship
        else:
            end_ship=col+length_ship
        if end_ship>size:
            print ("Please enter a valid position or orientation, the ship won't fit.")
        else:
            space=True

        while space and empty and not done:
            if orientation=="h":
                for i in range(0,length_ship):
                    if board[row][col] == "o":
                        col +=1
                    else:
                        empty=False
                done=True
            else:
                for i in range(0,length_ship):
                    if board[row][col] == "o":
                        row +=1
                    else:
                        empty=False
                done=True

        if empty and space:
            checked=True
        else:
            print ("The ship is overlapping with another ship. Please enter a valid orientation or position.")

    board=place_ship(p_col,p_row,length_ship,orientation,board)
    return board


def place_ships(board, player):
    if player==1:
        ships=[5,4,3,3,2]
        for i in range(0,5):
            board=check_and_add_ship(board, ships[i])
        return board
    else:
        return comp_board(board)

def create_board(sizeinput):
  toprow=[]
  size = sizeinput
  board=[]
  for toprownums in range(0, size+1):
    toprow.append(toprownums)
  board.append(toprow)

  for rowwise in range(1, size+1):
    row=[]
    row.append(rowwise)
    for col in range(0,size):
      row.append("o")
    board.append(row)

  game_board=board
  return board

def display_board(board):
    for row in board:
        print(" ".join(str(col) for col in row))

def gameover(anyboard):
    hitcount = 0
    for lst in anyboard:
        for item in lst:
            if item == "H":
                hitcount += 1
    if hitcount == 17:
        return True
    else:
        return False

def diff():
    difficultybool=False
    while not difficultybool:
        difficulty_level = input('please enter a level of difficulty easy or hard:')
        if difficulty_level == 'e' or difficulty_level == 'h':
            difficultybool=True
    return difficulty_level

def size(diff):
    if diff == "e":
        return 9
    else:
        return 12

def attack(turn, attack_pos, game_board_attack, game_board_user, game_board_comp):
    print(attack_pos)
    if turn ==1:
        if game_board_comp[int(attack_pos[0])][int(attack_pos[1])] == "o":
            game_board_comp[int(attack_pos[0])][int(attack_pos[1])] = "M"
            game_board_attack[int(attack_pos[0])][int(attack_pos[1])] ="M"
        if game_board_comp[int(attack_pos[0])][int(attack_pos[1])] == "S":
            game_board_comp[int(attack_pos[0])][int(attack_pos[1])] = "H"
            game_board_attack[int(attack_pos[0])][int(attack_pos[1])] ="H"
        else:
            print ("You just wasted a turn. This position was already attacked.")
        return [game_board_attack, game_board_comp]
    else:
        if game_board_user[int(attack_pos[0])][int(attack_pos[1])] == "o":
            game_board_user[int(attack_pos[0])][int(attack_pos[1])] = "M"
        else:
            game_board_user[int(attack_pos[0])][int(attack_pos[1])] ="H"
        return game_board_user

def play():
    game_board_user=[]
    game_board_comp=[]
    game_board_attack=[]
    turn=1

    print ("Welcome to Battleships!!")
    print ("Let's get started.")

    difficulty=diff()
    size_board=size(difficulty)

    game_board_comp=create_board(size_board)
    game_board_user=create_board(size_board)
    game_board_attack=create_board(size_board)

    print("MAKE YOUR BOARD: ")
    game_board_user = place_ships(game_board_user, 1)
    game_board_comp = place_ships(game_board_comp, 2)
    #place_ships(game_board_comp, 2)

    while( not gameover(game_board_user) and not gameover(game_board_attack)):
        if turn == 1:
            print("Let's attack!!")
            attack_pos=get_attack(turn,game_board_attack,game_board_user,difficulty)
            print("You are attacking at:")
            new_boards=attack(turn,attack_pos,game_board_attack,game_board_user,game_board_comp)
            game_board_attack = new_boards[0]
            game_board_comp = new_boards[1]
            print("Your current board: ")
            display_board(game_board_user)
        else:
            print("The computers turn: ")
            attack_pos=get_attack(turn,game_board_attack,game_board_user,difficulty)
            print("It takes a shot at:")
            new_boards=attack(turn,attack_pos,game_board_attack,game_board_user,game_board_comp)
            game_board_user = new_boards
            print("Your current now: ")
            display_board(game_board_user)
        turn=3-turn

    winner=3-turn

    if winner==1:
        print("YOU WIN!!")
    else:
        print("Awww that sucks! Better luck next time.")
