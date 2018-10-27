from konane import Game

game = Game()

initial = game.initialState
action = game.Actions(game.initialState)[0]
result = game.Result(initial, action)

print(str(initial))
print(game.Actions(initial))
print(game.TerminalTest(initial))
print(str(result))
print(game.Actions(result))
print(game.TerminalTest(result))
