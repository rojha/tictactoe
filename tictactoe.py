"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None

tabvalue = 0

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    board.
    Returns player who has the next turn on a board.
    """
    xcount = 0;
    ocount = 0;

    for row in range(0, 3) :
        for col in range(0, 3) :
            if board[row][col] == X :
                xcount += 1;
            if board[row][col] == O :
                ocount += 1;

    if xcount > ocount :
        return O;

    return X;            


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possibleActions = set();

    for row in range(0, 3) :
        for col in range(0, 3) :
            if board[row][col] == EMPTY :
                possibleActions.add((row, col));

    return possibleActions;

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]] != EMPTY :
        raise ValueError;

    # Create deep copy of board...
    copyofboard = copy.deepcopy(board);

    # Find player...
    currentPlayer = player(board);

    copyofboard[action[0]][action[1]] = currentPlayer;

    return copyofboard;

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    #Check rows
    wehaveawinner = None;
    for row in range(0, 3) :
        if board[row][0] == board[row][1] and board[row][1] == board[row][2] :
            wehaveawinner = board[row][0];
            break;

    # Check columns
    for col in range(0, 3) :
        if board[0][col] == board[1][col] and board[1][col] == board[2][col] :
            wehaveawinner = board[0][col];
            break;

    # Check diagonals
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] :
            wehaveawinner = board[0][0];

    if board[0][2] == board[1][1] and board[1][1] == board[2][0] :
            wehaveawinner = board[0][2];

    return wehaveawinner;

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    #Check if we have a winner 
    andthewinneris = winner(board);

    # No winner, is the board full?
    boardfull = True;

    if(andthewinneris == None) :
        for row in range(0, 3) :
            for col in range(0, 3) :
                if board[row][col] == EMPTY :
                    boardfull = False;
                    break;
    
    if andthewinneris != None or boardfull == True :
        return True;

    return False;


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    andthewinneris = winner(board);
    if andthewinneris == X :
        return 1;
    if andthewinneris == O :
        return -1;

    return 0;


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board) :
        return None;

    # Find current player
    currentPlayer = player(board);

    tabvalue = 0;

    if currentPlayer == X :
        value, actionvalue = maxValue(board);
        return actionvalue;

    if isboardempty(board) == True:
        return (1,1);

    value, actionvalue = minValue(board);

    return actionvalue;

def isboardempty(board) :
    for row in range(0, 3) :
        for col in range(0, 3) :
            if board[row][col] != EMPTY :
                return False;

    return True;

def maxValue(board) :
    value = -100;
    actionvalue = None;
    global tabvalue;

    if terminal(board) :
        return utility(board), None;

    # Get list of all possible actions 
    possibleActions = actions(board);
    
    for action in possibleActions :
        minvalue, actionprocessed = minValue(result(board, action));
        if( minvalue > value ) :
            value = minvalue;
            actionvalue = action;
        tabvalue = tabvalue + 1;

    return value, actionvalue;

def minValue(board) :
    value = 100;
    actionvalue = None;
    global tabvalue;

    if terminal(board) :
        return utility(board), None;

    # Get list of all possible actions 
    possibleActions = actions(board);
    
    for action in possibleActions :
        maxvalue, actionprocessed = maxValue(result(board, action));
        if( value >= maxvalue ) :
            actionvalue = action;
            value = maxvalue;

        tabvalue = tabvalue + 1;


    return value, actionvalue;
