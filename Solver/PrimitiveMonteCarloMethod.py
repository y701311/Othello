import numpy as np
from copy import deepcopy

from Board.Board import Board
from Board.Disc import Disc
from Solver.Solver import Solver
from Location.Location import Location

# 原始モンテカルロ法
class PrimitiveMonteCarloMethod(Solver):

    def __init__(self, samplingNum:int=100) -> None:
        self.samplingNum = samplingNum

    # 石を置く場所を選択する
    def selectLocation(self, board:Board) -> Location:
        placeableLocation = board.getPlaceableLocation()
        if len(placeableLocation) == 0:
            # 置ける場所が無いならパス
            return "pass"
        
        winRate = []
        for loc in placeableLocation:
            winNum = 0
            # 1手先の盤面
            oneMoveAheadBoard = deepcopy(board)
            oneMoveAheadBoard.put(loc)
            oneMoveAheadBoard.updateBoardStatus()
            for _ in range(self.samplingNum):
                # 1手先の盤面からランダムに進める
                copiedBoard = deepcopy(oneMoveAheadBoard)
                if self.playout(copiedBoard) == board.player:
                    winNum += 1
            winRate.append(winNum / self.samplingNum)
        maxWinRateIndex = np.argmax(winRate)
        
        # 勝った割合の最も大きい手を選択
        return placeableLocation[maxWinRateIndex]

    # ゲーム終了までランダムに石を置き続け、勝った石の色を返す
    def playout(self, board:Board) -> Disc:
        while not board.gameIsFinished():
            placeableLocation = board.getPlaceableLocation()
            if len(placeableLocation) != 0:
                loc = placeableLocation[np.random.randint(len(placeableLocation))]
                board.put(loc)
            else:
                board.passPut()
            board.updateBoardStatus()

        return board.getWinner()
