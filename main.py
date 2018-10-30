import sys
import time
from konane import Game
from evals import trivialEval

def mapArgToFunction(type):
    if type == 'trivial':
        return trivialEval

def gameRunner():
    game = Game()
    currentState = game.initialState
    count = 0
    while(not game.TerminalTest(currentState)):
        sys.stdout.write("\rActions taken %i" % count)
        sys.stdout.flush()
        action = game.Minimax(currentState, 2)
        # print(action)
        currentState = game.Result(currentState, action)
        # print(currentState)
        count += 1
    print('\nEnd: \n' + str(currentState))
    print('Black: ', game.Utility(currentState, 0)[0])
    print('White: ', game.Utility(currentState, 1)[0])
    print('Evals: ', game.numEvals)
    print('Branching: ', game.numBranches / game.numLevels)

inputOne = mapArgToFunction('trivial')
inputTwo = mapArgToFunction('trivial')

if len(sys.argv) == 1:
    inputOne = mapArgToFunction(sys.argv[0])
if len(sys.argv) == 2:
    inputTwo = mapArgToFunction(sys.argv[1])

gameRunner()




#
# game = Game()
#
# initial = game.initialState
# print(str(initial))
# print(game.Actions(initial))
# print(game.TerminalTest(initial))


# action = game.Actions(initial)[0]
# action = game.Minimax(initial, 2)
# result = game.Result(initial, action)
# print(str(result))
# print(game.Minimax(result, 3))
# print(game.TerminalTest(result))
# print(game.numEvals)
# print(game.numBranches, game.numLevels)
