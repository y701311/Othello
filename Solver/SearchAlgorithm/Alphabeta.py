from math import inf
from copy import deepcopy

from Board.Board import Board
from Location.Location import Location
from Solver.Solver import Solver
from Solver.EvaluationFunction.EvaluationFunction import EvaluationFunction

# アルファベータ法
class Alphabeta(Solver):

    def __init__(self, evaluationFunction:EvaluationFunction, depth:int) -> None:
        self.evaluationFunction = evaluationFunction
        self.depth = depth

    # 石を置く場所を選択する
    def selectLocation(self, board:Board) -> Location:
        self.player = board.player

        placeableLocation = board.getPlaceableLocation()
        if len(placeableLocation) == 0:
            # 置ける場所が無いならパス
            return "pass"
        
        evaluationValue = []
        for loc in placeableLocation:
            # 1手先の盤面
            oneMoveAheadBoard = deepcopy(board)
            oneMoveAheadBoard.put(loc)
            evaluationValue.append(self.alphabeta(oneMoveAheadBoard, self.depth, -inf, inf))
        maxEvaluationValue = max(evaluationValue)
        for i, value in enumerate(evaluationValue):
            if value == maxEvaluationValue:
                maxEvaluationValueIndex = i
        
        # 評価値の最も大きい手を選択
        return placeableLocation[maxEvaluationValueIndex]

    # アルファベータ法
    def alphabeta(self, board:Board, depth:int, alpha:int, beta:int) -> float:
        if board.gameIsFinished() or depth == 0:
            return self.evaluationFunction.evaluate(board)
        
        placeableLocation = board.getPlaceableLocation()
        if len(placeableLocation) == 0:
            board.passPut()
            board.updateBoardStatus()
            if board.player == self.player:
                alpha = max(alpha, self.alphabeta(board, depth-1, alpha, beta))
                return alpha
            else:
                beta = min(beta, self.alphabeta(board, depth-1, alpha, beta))
                return beta

        if board.player == self.player:
            for loc in placeableLocation:
                oneMoveAheadBoard = deepcopy(board)
                oneMoveAheadBoard.put(loc)
                oneMoveAheadBoard.updateBoardStatus()
                alpha = max(alpha, self.alphabeta(oneMoveAheadBoard, depth-1, alpha, beta))
                if alpha >= beta:
                    break # betaカット
            return alpha
        else:
            for loc in placeableLocation:
                oneMoveAheadBoard = deepcopy(board)
                oneMoveAheadBoard.put(loc)
                oneMoveAheadBoard.updateBoardStatus()
                beta = min(beta, self.alphabeta(oneMoveAheadBoard, depth-1, alpha, beta))
                if alpha >= beta:
                    break # alphaカット
            return beta
