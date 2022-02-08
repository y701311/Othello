import numpy as np
from copy import deepcopy

from Board.Board import Board
from Location.Location import Location
from Solver.Solver import Solver
from Solver.EvaluationFunction.EvaluationFunction import EvaluationFunction
from Solver.SearchAlgorithm.MonteCarloTreeSearch.Node import Node

# モンテカルロ木探索
class MonteCarloTreeSearch(Solver):

    def __init__(self, samplingNum:int=50, expandBase:int=5, selectChildNodeAlgorithm:str="UTC", evaluationFunction:EvaluationFunction=None) -> None:
        self.samplingNum = samplingNum
        self.expandBase = expandBase
        self.evaluationFunction = evaluationFunction
        self.selectChildNodeAlgorithm = selectChildNodeAlgorithm

    # 石を置く場所を選択する
    def selectLocation(self, board:Board) -> Location:
        placeableLocation = board.getPlaceableLocation()
        if len(placeableLocation) == 0:
            # 置ける場所が無いならパス
            return "pass"
        
        return self.monteCarloTreeSearch(board)

    # モンテカルロ木探索
    def monteCarloTreeSearch(self, board:Board) -> Location:
        root = Node(deepcopy(board), None, None)

        for _ in range(self.samplingNum):
            node = root

            # Selection
            while len(node.untriedLocations) == 0 and len(node.childNodes) != 0:
                node = node.selectChildNode(self.selectChildNodeAlgorithm, None)
            
            # Expansion
            if (len(node.untriedLocations) != 0 and node.visitNum == self.expandBase) or (node == root):
                node = node.expandChild()

            # Simulation
            winner = node.playout()

            # Backpropagation
            node.backpropagation(winner)

        # 相手番の試行回数が最小の手を選ぶ
        visitNums = []
        for child in root.childNodes:
            visitNums.append(child.visitNum)
        index = np.argmin(visitNums)
        return root.childNodes[index].location
