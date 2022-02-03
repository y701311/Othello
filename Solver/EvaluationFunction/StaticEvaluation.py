from Solver.EvaluationFunction.EvaluationFunction import EvaluationFunction
from Board.Board import Board
from Location.Location import Location

# 静的評価関数
class StaticEvaluationFunction(EvaluationFunction):

    def __init__(self) -> None:
        # 盤面のマスごとの評価値
        self.evalValueBoard = [
            [30, -12, 0, -1, -1, 0, -12, 30],
            [-12, -15, -3, -3, -3, -3, -15, -12],
            [0, -3, 0, -1, -1, 0, -3, 0],
            [-1, -3, -1, -1, -1, -1, -3, -1],
            [-1, -3, -1, -1, -1, -1, -3, -1],
            [0, -3, 0, -1, -1, 0, -3, 0],
            [-12, -15, -3, -3, -3, -3, -15, -12],
            [30, -12, 0, -1, -1, 0, -12, 30],
        ]

    # 盤面の評価値を返す
    def evaluate(self, board:Board) -> float:
        evaluationValue = 0
        loc = Location()

        for i in range(1, 9):
            for j in range(1, 9):
                loc.row = i
                loc.column = j
                if board.getLocationDisc(loc) == board.player:
                    evaluationValue += self.evalValueBoard[i-1][j-1]
        
        return evaluationValue
