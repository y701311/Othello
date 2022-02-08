from Location.Location import Location
from Board.Board import Board
from Solver.Solver import Solver
from Solver.SearchAlgorithm.MonteCarloTreeSearch.MonteCarloTreeSearch import MonteCarloTreeSearch

# 評価関数を用いないモンテカルロ木探索のソルバー
class MCTS(Solver):

    def __init__(self, samplingNum:int=50, expandBase:int=5, selectChildNodeAlgorithm:str="UTC"):
        self.search = MonteCarloTreeSearch(samplingNum=samplingNum, expandBase=expandBase, selectChildNodeAlgorithm=selectChildNodeAlgorithm)

    # 石を置く場所を選択する
    def selectLocation(self, board:Board) -> Location:
        return self.search.selectLocation(board)
