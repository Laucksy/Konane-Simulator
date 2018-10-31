def trivialEval(game, state):
    # print("Evaluation")
    # print(state)
    # print(state.turn)
    # print("a")
    # print(self.Actions(state))
    return (0.5, None)

def nextMovesEval(game, state):
    return (len(game.Actions(state)), None)
