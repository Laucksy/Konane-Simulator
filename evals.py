def trivialEval(game, state):
    # print("Evaluation")
    # print(state)
    # print(state.turn)
    # print("a")
    # print(self.Actions(state))
    return (0.5, game.Actions(state)[0])
