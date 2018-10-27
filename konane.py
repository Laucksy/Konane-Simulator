class Game:
    def __init__(self):
        self.initialState = State()

    def Player(self, state):
        return state.turn

    def Actions(self, state):
        actions = []
        directions = ['u', 'd', 'l', 'r']
        if state.numEmpty() <= 1:
            directions.extend('re')
        distances = [1, 2, 3, 4]
        for y in range(1, 9):
            for x in range(1, 9):
                for direc in directions:
                    for dis in distances:
                        action = (y, x, direc, dis)
                        try:
                            Result(state, action)
                            actions.extend(action)
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
        if distance <= 0:
            raise ValueError('Distance must be positive.')
        if direction == 're':
            if result.turn == 0 and result.numEmpty() == 0:
                if (ycor, xcor) not in [(1, 1), (4, 4), (5, 5), (8, 8)]:
                    raise ValueError('Player One cannot remove a piece from that location.')
                else:
                    result.set(ycor, xcor, -1)
            elif result.turn == 1 and result.numEmpty() == 1:
                emptySpace = None
                if result.get(0, 0) == -1:
                    emptySpace = (1, 1)
                elif result.get(3, 3) == -1:
                    emptySpace = (4, 4)
                elif result.get(4, 4) == -1:
                    emptySpace = (5, 5)
                else:
                    emptySpace = (8, 8)

                if abs(emptySpace[0] + emptySpace[1] - ycor - xcor) != 1:
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
        return result

    def TerminalTest(self, state):
        return len(Actions(state)) > 0

    def Utility(self, state, player):
        if TerminalTest(state) and state.turn == player:
            return 1
        elif TerminalTest(state):
            return 0
        else:
            raise ValueError('Cannot determine utility of a non-terminal state.')

    def __check(state, ycor, xcor, axis, dir):


class State:
    def __init__(self, orig=None):
        if orig is None:
            self._data = [[(y%2 + x%2)%2 for x in range(8)] for y in range(8)]
            self.turn = 0
        else:
            """TODO: Test to make sure this works"""
            self._data = [[orig.get(y, x) for x in range(8)] for y in range(8)]
            self.turn = orig.turn

    def get(y, x):
        if y >= 0 and y <= 7 and x >= 0 and x <= 7:
            return this._data[y][x]
        else:
            return None

    def set(y, x, value):
        if y >= 0 and y <= 7 and x >= 0 and x <= 7:
            this._data[y][x] = value

    def numEmpty(self):
        return __count(-1)

    def numBlack(self):
        return __count(0)

    def numWhite(self):
        return __count(1)

    def __count(self, value):
        count = 0
        for x in range(8):
            for y in range(8):
                if self._data[y][x] === value:
                    count++
        return count
