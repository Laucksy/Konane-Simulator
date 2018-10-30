import sys
from konane import Game
from evals import trivialEval

# def mapArgToFunction(type):
#     if type == 'trivial':
#         return trivialEval
#
# def gameRunner():
#     print('here')
#     game = Game()
#     currentState = game.initalState
#     while(not TerminalTest(currentState)):
#         if currentState.turn == 0:
#             currentState = game.Result(currentState, game.Actions(currentState)[0])
#         else:
#             currentState = game.Result(currentState, game.Actions(currentState)[0])
#     print(currentState)
#     print(game.Utility(currentState, 0))
#     print(game.Utility(currentState, 1))
#
# inputOne = mapArgToFunction('trivial')
# inputTwo = mapArgToFunction('trivial')
#
# if len(sys.argv) == 1:
#     inputOne = mapArgToFunction(sys.argv[0])
# if len(sys.argv) == 2:
#     inputTwo = mapArgToFunction(sys.argv[1])
#
# gameRunner()





game = Game()

initial = game.initialState
# print(str(initial))
# print(game.Actions(initial))
# print(game.TerminalTest(initial))


# action = game.Actions(initial)[0]
action = game.Minimax(initial, 3)
result = game.Result(initial, action)
print(str(result))
print(game.Minimax(result, 3)) 
print(game.TerminalTest(result))

# action = game.Actions(result)[0]
# result = game.Result(result, action)
# print(str(result))
# print(game.Actions(result))
# print(game.TerminalTest(result))

# action = game.Actions(result)[0]
# result = game.Result(result, action)
# print(str(result))
# print(game.Actions(result))
# print(game.TerminalTest(result))

# action = game.Actions(result)[0]
# result = game.Result(result, action)
# print(str(result))
# print(game.Actions(result))
# print(game.TerminalTest(result))

# action = game.Actions(result)[0]
# result = game.Result(result, action)
# print(str(result))
# print(game.Actions(result))
# print(game.TerminalTest(result))

# action = game.Actions(result)[0]
# result = game.Result(result, action)
# print(str(result))
# print(game.Actions(result))
# print(game.TerminalTest(result))
