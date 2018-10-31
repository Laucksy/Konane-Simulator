class Game:
    def __init__(self, evalOne, evalTwo):
        self.evalOne = evalOne
        self.evalTwo = evalTwo
        self.initialState = State()
        self.numEvals = 0
        self.numBranches = 0
        self.numLevels = 0
        self.numPruned = 0


    def Player(self, state):
        return state.turn

    def Actions(self, state):
        actions = []
        directions = ['u', 'd', 'l', 'r']
        if state.numEmpty() <= 1:
            directions.append('re')
        distances = [1, 2, 3, 4]
        for y in range(1, 9):
            for x in range(1, 9):
                if state.get(y-1, x-1) != state.turn:
                    continue
                for direc in directions:
                    for dis in distances:
                        action = (y, x, direc, dis)
                        try:
                            self.Result(state, action)
                            actions.append(action)
                        except:
                            continue
        return actions

    def Result(self, state, action):
        ycor = action[0] - 1
        xcor = action[1] - 1
        direction = action[2]
        distance = action[3]
        result = State(state)
        opponent = 1 if result.turn == 0 else 0

        if result.get(ycor, xcor) != result.turn:
            raise ValueError('The specified piece does not belong to the current player.')
        if distance <= 0 or (direction == 're' and distance > 1):
            raise ValueError('Distance must be positive.')
        if direction == 're':
            if result.turn == 0 and result.numEmpty() == 0:
                if (ycor, xcor) not in [(0, 0), (3, 3), (4, 4), (7, 7)]:
                    raise ValueError('Player One cannot remove a piece from that location.')
                else:
                    result.set(ycor, xcor, -1)
            elif result.turn == 1 and result.numEmpty() == 1:
                emptySpace = None
                if result.get(0, 0) == -1:
                    emptySpace = (0, 0)
                elif result.get(3, 3) == -1:
                    emptySpace = (3, 3)
                elif result.get(4, 4) == -1:
                    emptySpace = (4, 4)
                else:
                    emptySpace = (7, 7)

                if abs(emptySpace[0] - ycor) + abs(emptySpace[1] - xcor) > 1:
                    raise ValueError('Player Two must pick a piece adjacent to the empty space.')
                else:
                    result.set(ycor, xcor, -1)
            else:
                raise ValueError('This move is not available at this time.')
        elif direction in ['u', 'd', 'l', 'r']:
            ymult = -1 if direction == 'u' else (1 if direction == 'd' else 0)
            xmult = -1 if direction == 'l' else (1 if direction == 'r' else 0)
            for x in range(0, distance):
                if result.get(ycor+ymult*(2*x+1), xcor+xmult*(2*x+1)) == opponent and result.get(ycor+ymult*(2*x+2), xcor+xmult*(2*x+2)) == -1:
                    result.set(ycor+ymult*(2*x), xcor+xmult*(2*x), -1)
                    result.set(ycor+ymult*(2*x+1), xcor+xmult*(2*x+1), -1)
                    result.set(ycor+ymult*(2*x+2), xcor+xmult*(2*x+2), result.turn)
                else:
                    raise ValueError('Invalid move.')

        result.turn = (result.turn+1)%2
        return result

    def TerminalTest(self, state):
        return len(self.Actions(state)) == 0

    def Utility(self, state, player):
        if self.TerminalTest(state) and state.turn == player:
            return (0, None)
        elif self.TerminalTest(state):
            return (1, None)
        else:
            raise ValueError('Cannot determine utility of a non-terminal state.')

    def Evaluation(self, state):
        self.numEvals += 1
        return self.evalOne(self, state) if state.turn == 0 else self.evalTwo(self, state)

    def Minimax(self, state, depthLimit, pruning = False):
        infinity = float('inf')
        result = self.max_value(state, -infinity if pruning else None, infinity if pruning else None, 0, depthLimit)
        return result[1];

    def max_value(self, state, alpha, beta, depth, depthLimit):
        if (self.TerminalTest(state)):
            return self.Utility(state, state.turn)
        elif (depth >= depthLimit):
            return self.Evaluation(state)

        v = -float('inf')
        s = None
        self.numBranches += len(self.Actions(state))
        self.numLevels += 1
        for a in self.Actions(state):
            result = self.min_value(self.Result(state, a), alpha, beta, depth+1, depthLimit)
            if (result[0] > v):
                v = result[0]
                s = a
            if alpha is not None and beta is not None:
                if v >= beta:
                    self.numPruned += 1
                    return (v, s)
                alpha = max(alpha, v)
        return (v, s)


    def min_value(self, state, alpha, beta, depth, depthLimit):
        if (self.TerminalTest(state)):
            return self.Utility(state, state.turn)
        elif (depth >= depthLimit):
            return self.Evaluation(state)

        v = float('inf')
        s = None
        self.numBranches += len(self.Actions(state))
        self.numLevels += 1
        for a in self.Actions(state):
            result = self.max_value(self.Result(state, a), alpha, beta, depth+1, depthLimit)
            if result[0] < v:
                v = result[0]
                s = a
            if alpha is not None and beta is not None:
                if v <= alpha:
                    self.numPruned += 1
                    return (v, s)
                beta = min(beta, v)
        return (v, s)



class State:
    def __init__(self, orig=None):
        if orig is None:
            self._data = [[(y%2 + x%2)%2 for x in range(8)] for y in range(8)]
            # self._data = [[0,-1,-1,-1,-1,-1,0,-1],[-1,-1,1,-1,-1,0,-1,-1],[0,-1,-1,-1,-1,-1,0,-1],[-1,-1,-1,-1,-1,-1,-1,-1],[-1,1,-1,-1,-1,1,-1,1],[1,0,1,0,1,0,1,0],[0,1,0,1,0,1,0,1],[1,0,1,0,1,0,1,0]]
            # print(self)
            self.turn = 0
        else:
            """TODO: Test to make sure this works"""
            self._data = [[orig.get(y, x) for x in range(8)] for y in range(8)]
            self.turn = orig.turn

    def __str__(self):
        string = ''
        for y in range(0, 8):
            for x in range(0, 8):
                char = ' '
                if self._data[y][x] == 0:
                    char = 'B'
                elif self._data[y][x] == 1:
                    char = 'W'
                string = string + str(char) + ' '
            string = string + '\n'
        return string


    def get(self, y, x):
        if y >= 0 and y <= 7 and x >= 0 and x <= 7:
            return self._data[y][x]
        else:
            return None

    def set(self, y, x, value):
        if y >= 0 and y <= 7 and x >= 0 and x <= 7:
            self._data[y][x] = value

    def numEmpty(self):
        return self.__count(-1)

    def numBlack(self):
        return self.__count(0)

    def numWhite(self):
        return self.__count(1)

    def __count(self, value):
        count = 0
        for x in range(8):
            for y in range(8):
                if self._data[y][x] == value:
                    count+=1
        return count
