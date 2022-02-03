from Board.Board import Board
from Solver.EvaluationFunction.StaticEvaluation import StaticEvaluationFunction
from Solver.SearchAlgorithm.Alphabeta import Alphabeta
from Solver.Solver import Solver
from Location.Location import Location
from Board.Board import Board

# 評価関数をStaticEvaluationとしてAlphabeta探索を行う
class StaticEval_Alphabeta(Solver):
    
    def __init__(self, depth:int=5) -> None:
        self.search = Alphabeta(StaticEvaluationFunction(), depth)

    # 石を置く場所を選択する
    def selectLocation(self, board:Board) -> Location:
        return self.search.selectLocation(board)
