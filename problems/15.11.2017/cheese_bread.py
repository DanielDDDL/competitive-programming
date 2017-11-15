# ------------- FUNCTIONS ---------------

# return a new board with all breads reaplaced with 9
def turn_all_breads_into_nines(board):
  for i in range(len(board)):
    for j in range(len(board[i])):
      if board[i][j] == 1:
        board[i][j] = 9

  return board


# return how many breads are around a certain position
def count_breads_around(board, x, y):

  count = 0

  # up
  if not y == 0:
    if board[x][y - 1] == 9:
      count += 1

  # down
  if not y >= len(board[0]) - 1:
    if board[x][y + 1] == 9:
      count += 1

  # left
  if not x == 0:
    if board[x - 1][y] == 9:
      count += 1

  # right
  if not x >= len(board) - 1:
    if board[x + 1][y] == 9:
      count += 1

  return count

# return all new board with all 0 replaced
# with their respective count
def replace_all_with_count(board):
  for i in range(len(board)):
    for j in range(len(board[i])):
      if not board[i][j] == 9:
        board[i][j] = count_breads_around(board,i,j)

  return board

# print the board as asked by the problem
def print_board(board):
  for i in range(len(board)):
    line = ""
    for j in range(len(board[i])):
      line += str(board[i][j])

    print(line)

# -------------  PROGRAM -------------
while True:
  try:
    # 0 - lines
    # 1 - columns
    info_board = [int(x) for x in input().rstrip().split(" ")]
    board = []

    for i in range(info_board[0]):
      line = [int(x) for x in input().rstrip().split(" ")]
      board.append(line)

    board = turn_all_breads_into_nines(board)
    board = replace_all_with_count(board)

    print_board(board)

  except:
    break

  
