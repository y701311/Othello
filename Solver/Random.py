import numpy as np

from Solver.Solver import Solver
from Location.Location import Location
from Board.Board import Board

# ランダムに置けるところに置く
class Random(Solver):

    # 石を置く場所を選択する
    def selectLocation(self, board:Board) -> Location:
        placeableLocation = board.getPlaceableLocation()
        if len(placeableLocation) == 0:
            return "pass"
        else:
            index = np.random.randint(len(placeableLocation))
            return placeableLocation[index]
