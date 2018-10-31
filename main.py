import sys
import time
from konane import Game
from evals import trivialEval

def mapArgToFunction(type):
    if type == 'manual':
        return type
    else:
        return trivialEval

def gameRunner(evalOne, evalTwo, depthLimit, pruning, printing):
    game = Game(evalOne if evalOne != 'manual' else evalTwo, evalTwo if evalTwo != 'manual' else evalOne)
    currentState = game.initialState
    count = 0
    while(not game.TerminalTest(currentState)):
        if (currentState.turn == 0 and evalOne == 'manual') or (currentState.turn == 1 and evalTwo == 'manual'):
            y = int(raw_input("Enter the y coordinate for the piece you want to move: "))
            x = int(raw_input("Enter the x coordinate for the piece you want to move: "))
            direction = raw_input("Enter the direction ('u', 'd', 'l', 'r', 're') for the piece you want to move: ")
            distance = int(raw_input("Enter the number of jumps for the piece you want to move: "))
            action = (y, x, direction, distance)
        else:
            action = game.Minimax(currentState, 2, pruning)

        try:
            currentState = game.Result(currentState, action)
        except Exception as e:
            print('\n\n' + str(e) + '\n')
            continue

        if printing:
            print(currentState)
        else:
            sys.stdout.write("\rActions taken %i" % count)
            sys.stdout.flush()
            count += 1
    print('\nEnd: \n' + str(currentState))
    print('Black: ', game.Utility(currentState, 0)[0])
    print('White: ', game.Utility(currentState, 1)[0])
    print('Evals: ', game.numEvals)
    print('Branching: ', (100 * game.numBranches / game.numLevels) / 100.0)
    print('Number of Times Pruned: ', game.numPruned)

inputOne = mapArgToFunction(sys.argv[1]) if len(sys.argv) >= 2 else mapArgToFunction('trivial')
inputTwo = mapArgToFunction(sys.argv[2]) if len(sys.argv) >= 3 else  mapArgToFunction('trivial')
inputThree = int(sys.argv[3]) if len(sys.argv) >= 4 else 3
inputFour = True if len(sys.argv) >= 5 and sys.argv[4] == "true" else False
inputFive = True if len(sys.argv) >= 6 and sys.argv[5] == "true" else False

gameRunner(inputOne, inputTwo, inputThree, inputFour, inputFive)




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
