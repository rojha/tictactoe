import tictactoe as ttt
import collections

X = "X"
O = "O"
EMPTY = None

def main() :
	# Run tests
	testPlayer();

	testTerminal();
	
	testAction();

	testResult();

	#testWinner();
	#testUtility();

def testResult() :
	print("Testing Result cases...");

	emptytestboard = [[EMPTY, EMPTY, EMPTY],
            		[EMPTY, EMPTY, EMPTY],
            		[EMPTY, EMPTY, EMPTY]];

	emptytestboardresult = [[EMPTY, EMPTY, EMPTY],
            		[X, EMPTY, EMPTY],
            		[EMPTY, EMPTY, EMPTY]];

	action = (1, 0);

	print("Action - ", emptytestboardresult[action[0]][action[1]]);
	testResultScenario(emptytestboard, "Valid action", action, X);

	invalidactiontestboard = [[X, O, EMPTY],
            		[EMPTY, EMPTY, EMPTY],
            		[EMPTY, EMPTY, EMPTY]];

	action = (0, 0);

	testResultScenario(invalidactiontestboard, "Invalid action", action, "ValueError");

def testResultScenario(testboard, testName, action, expectedResult) :
    
	try:
		result = ttt.result(testboard, action);		

		value = result[action[0]][action[1]];
		if  value != expectedResult :
			print ("  ", testName, " - failed. Got - ", result[action[0]][action[1]], ", Expecting - ", expectedResult);
		else :
			print ("  ", testName, " - success");
	except ValueError:
	    if expectedResult != "ValueError" :
	    	print ("  ", testName, " - failed. Got ValueError exception");
	    else :
	    	print ("  ", testName, " - success");
		  	

def testAction() :
	print ("Testing Action cases ...");
	emptytestboard = [[EMPTY, EMPTY, EMPTY],
            		[EMPTY, EMPTY, EMPTY],
            		[EMPTY, EMPTY, EMPTY]];

	result = {(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)};

	testActionScenario(emptytestboard, "Empty board", result);

	print ("Testing Action cases ...");
	testboard1 = [[X, EMPTY, EMPTY],
            		[EMPTY, O, EMPTY],
            		[EMPTY, EMPTY, O]];

	result1 = {(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)};

	testActionScenario(testboard1, "Filled board 1", result1);

def testActionScenario(testboard, testName, expectedResult) :
    result = ttt.actions(testboard);

    comparedSet = result.difference(expectedResult);

    if len(comparedSet) != 0 :
    	print ("  ", testName, " - failed. Got - ", result, ", Expecting - ", expectedResult);
    else :
    	print ("  ", testName, " - success");


def testTerminal() :
	print ("Testing Terminal cases ...");
	emptytestboard = [[EMPTY, EMPTY, EMPTY],
            		[EMPTY, EMPTY, EMPTY],
            		[EMPTY, EMPTY, EMPTY]];

	testTerminalScenario(emptytestboard, "Empty board", False);

	testboardPartial1 = [[X, EMPTY, EMPTY],
            	[EMPTY, EMPTY, EMPTY],
            	[EMPTY, EMPTY, EMPTY]];

	testTerminalScenario(testboardPartial1, "Partial 1", False);

	testboardPartial2 = [[X, O, O],
            	[EMPTY, X, EMPTY],
            	[EMPTY, EMPTY, EMPTY]];

	testTerminalScenario(testboardPartial2, "Partial 2", False);

	testboardFull = [[X, O, X],
            		[X, O, O],
            		[O, X, X]];

	testTerminalScenario(testboardFull, "No winner board", True);

	testboardXWins = [[X, O, EMPTY],
            		[X, O, EMPTY],
            		[X, EMPTY, EMPTY]];

	testTerminalScenario(testboardXWins, "X wins", True);

	testboardOWins = [[O, X, EMPTY],
            		[O, X, EMPTY],
            		[O, EMPTY, EMPTY]];
	testTerminalScenario(testboardOWins, "O wins", True);

	testColumnWinTerminalScenario();
	testRowWinTerminalScenario();

def testColumnWinTerminalScenario() :
	testboardCol1Wins = [[O, X, O],
            		[O, X, EMPTY],
            		[O, EMPTY, EMPTY]];
	testTerminalScenario(testboardCol1Wins, "Col1 wins", True);

	testboardCol2Wins = [[O, X, O],
            		[X, X, EMPTY],
            		[O, X, EMPTY]];
	testTerminalScenario(testboardCol1Wins, "Col2 wins", True);

	testboardCol3Wins = [[O, X, O],
            		[X, X, O],
            		[O, EMPTY, O]];
	testTerminalScenario(testboardCol1Wins, "Col3 wins", True);

def testRowWinTerminalScenario() :
	testboardRow1Wins = [[X, X, X],
            		[O, X, EMPTY],
            		[O, EMPTY, EMPTY]];
	testTerminalScenario(testboardRow1Wins, "Row1 wins", True);

	testboardRow2Wins = [[X, X, O],
            		[O, O, O],
            		[O, EMPTY, EMPTY]];
	testTerminalScenario(testboardRow2Wins, "Row2 wins", True);

	testboardRow3Wins = [[X, X, O],
            		[O, X, EMPTY],
            		[O, O, O]];
	testTerminalScenario(testboardRow3Wins, "Row3 wins", True);


def testTerminalScenario(testboard, testName, expectedResult) :
    result = ttt.terminal(testboard);
    if result != expectedResult :
    	print ("  ", testName, " - failed. Got - ", result, ", Expecting - ", expectedResult);
    else :
    	print ("  ", testName, " - success");

def testPlayer() :
	print ("Testing Player ...");

	emptytestboard = [[EMPTY, EMPTY, EMPTY],
            		[EMPTY, EMPTY, EMPTY],
            		[EMPTY, EMPTY, EMPTY]];

	testPlayerScenario(emptytestboard, "Empty board", X);

	testboardO = [[X, EMPTY, EMPTY],
            	[EMPTY, EMPTY, EMPTY],
            	[EMPTY, EMPTY, EMPTY]];

	testPlayerScenario(testboardO, "O turn", O);

	testboardX = [[X, O, EMPTY],
            	[EMPTY, EMPTY, EMPTY],
            	[EMPTY, EMPTY, EMPTY]];

	testPlayerScenario(testboardX, "X turn", X);

	testboardFull = [[X, O, X],
            		[O, X, O],
            		[X, O, X]];

	testPlayerScenario(testboardFull, "Full board", O);

	testboardXWins = [[X, O, EMPTY],
            		[X, O, EMPTY],
            		[X, EMPTY, EMPTY]];

	testPlayerScenario(testboardXWins, "X wins", O);

	testboardOWins = [[O, X, EMPTY],
            		[O, X, EMPTY],
            		[O, EMPTY, EMPTY]];
	testPlayerScenario(testboardOWins, "O wins", X);

def testPlayerScenario(testboard, testName, expectedPlayer) :
    player = ttt.player(testboard);
    if player != expectedPlayer :
    	print ("  ", testName, " - failed. Got - ", player, ", Expecting - ", expectedPlayer);
    else :
    	print ("  ", testName, " - success");

if __name__ == "__main__":
    main()

