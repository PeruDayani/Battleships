def get_attack (turn, game_board_attack, game_board_user, diff):
  if turn == 1:
    move = user_move(game_board_attack)
  else:
    move = comp_move(game_board_user, diff)
  return move

def user_move(game_board_attack):
  valid = False
  show_board(game_board_attack)
  while not valid :
    attackcol = input('please enter column number of attack:')
    attackrow = input('please enter row number of attack:')
    if  attackcol.isdigit() and int(attackcol) <= size and int(attackcol)>0 and attackrow.isdigit() and int(attackrow) <= size and int(attackrow)>0 :
    	move = [attackrow,attackcol]
      valid = true
      return move
    else:
      print ("please try again with integers between 1 and 9 for both inputs")

def hard_move(game_board_user):
  listofships = []
  listofsea = []
  for i in game_board_user :
      for j in list :
        if game_board_user[i][j]=='s':
          listofships.append([i, j])
      	elif game_board_user[i][j] == 'o':
          listofsea.append([i, j])
  decider = (random.randint(1,5))
  if decider >= 4 :
    return random.choice(listofships)
  else:
    return random.choice(listofsea)

def easy_move(game_board_user):
  import random
      attackrow=(random.randint(1,9))
      attackcol=(random.randint(1,9))
      move = [attackrow,attackcol]
      return move

def comp_move(game_board_user, diff):
  if diff == 'e':
    return easy_move(game_board_user)
  else
  	return hard_move(game_board_user)

def place_ship(col, row, length, orientation, board):
    if orientation == "v":
        board[row][col] = "S"
        for i in range(length-1):
            board[row+i+1][col] = "S"
    else:
        board[row][col] = "S"
        for x in range(length-1):
            board[row][col+x+1] = "S"
    return board

def comp_board(board):
    ships= [5,4,3,3,2]
    for i in range(len(ships)):
        board= place_ship(i+1,1,ships[i],'v',board)
    return board


def check_and_add_ship(board, length_ship):
    col = False
    row = False
    orientation = False
    size=len(board)
    checked=False
    empty=False

    while not checked:
        print ("Place the ship of length: " + str(length_ship))

        display_board(board)

        while not orientation:
            orientation = input('Please enter orientation (h,v) : ')
            if orientation != 'v' or orientation != 'h':
                orientation=False
                print ('Invalid orientation. Try entering v or h')

        while not col:
            col = input('Please enter column coordinate:')
            if !(col.isdigit() and int(col) <= size and int(col)>0):
                col=False
                print ('Invalid column. Try entering a number between 1 and ' + str(size))

        while not row:
            row = input('Please enter column coordinate:')
            if !(row.isdigit() and int(row) <= size and int(row)>0):
                row=False
                print ('Invalid row. Try entering a number between 1 and ' + str(size))

        if orientation=='v':
            end_ship=row+length_ship
        else:
            end_ship=col+length_ship
        if end_ship>size:
            "Please enter a valid position or orientation, the ship won't fit."
        else:
            space=True

        while space and !empty:
            empty=True
            if orientation=='h':
                for i in range(0,length_ship):
                    if board[row][col] == 'o':
                        col +=1
                    else:
                        empty=False
            else:
                for i in range(0,length_ship):
                    if board[row][col] == 'o':
                        row +=1
                    else:
                        empty=False

        if empty and space:
            checked=True
        else:
            print ("The ship is overlapping with another ship. Please enter a valid orientation or position.")

    board=place_ship(col,row,length_ship,orientation,board)
    return board


def place_ships(board, player):
    if player==1:
        ships=[5,4,3,3,2]
        for i in range(0,5):
            board=check_and_add_ship(board, ships[i])
        return board
    else
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
      row.append('o')
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
            if item == 'h':
                hitcount += 1
    if hitcount= 17:
        return True
    else:
        return False

def difficulty():
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

def attack(turn, attack_pos, game_board_user, game_board_attack, game_board_comp):
    if turn ==1:
        if game_board_comp[attack_pos[0]][attack_pos[1]] == 'o':
            game_board_comp[attack_pos[0]][attack_pos[1]] = 'M'
            game_board_attack[attack_pos[0]][attack_pos[1]] ='M'
        elif game_board_comp[attack_pos[0]][attack_pos[1]] == 'S':
            game_board_comp[attack_pos[0]][attack_pos[1]] = 'H'
            game_board_attack[attack_pos[0]][attack_pos[1]] ='H'
        else:
            print ("You just wasted a turn. This position was already attacked.")
        return [game_board_attack, game_board_comp]
    else:
        if game_board_user[attack_pos[0]][attack_pos[1]] == 'o':
            game_board_user[attack_pos[0]][attack_pos[1]] = 'M'
        else:
            game_board_user[attack_pos[0]][attack_pos[1]] ='H'
        return game_board_user

def play():
    game_board_user=[]
    game_board_comp=[]
    game_board_attack=[]
    turn=1

    print ("Welcome to Battleships!!")
    print ("Let's get started.")

    difficulty=difficulty()
    size_board=size(difficulty)

    game_board_attack=create_board(size_board)
    game_board_user=create_board(size_board)
    game_board_attack=create_board(size_board)

    game_board_user = place_ships(game_board_user, 1)
    game_board_comp = place_ships(game_board_comp, 2)

    while( !gameover(game_board_user) and !gameover(game_board_attack)):
        attack_pos=get_attack(turn,game_board_attack,game_board_user,difficulty)
        new_boards=attack(turn,game_board_attack,game_board_user,game_board_comp,attack_pos)
        if turn == 2:
            game_board_user = new_boards
        else:
            game_board_attack = new_boards[0]
            game_board_comp = new_boards[1]
        turn=3-turn

    winner=3-turn

    if winner==1:
        print("you win!!")
    else:
        print("you suck!")
