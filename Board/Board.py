from Location.Location import Location
from Board.Disc import Disc

# オセロの盤
class Board:

    def __init__(self) -> None:
        # 打っているプレイヤーの色
        self.player = Disc.black

    # 指定された場所に置く
    def put(self, location:Location) -> None:
        pass

    # パスをする
    def passPut(self) -> None:
        pass

    # 指定された場所に置けるかどうか
    def canPut(self, location:Location) -> bool:
        pass

    # 置ける場所をLocationのlistとして返す
    def getPlaceableLocation(self) -> list:
        pass

    # 反転処理
    def reverse(self) -> None:
        pass

    # ボードのパラメータを更新
    def updateBoardStetus(self):
        pass

    # 石の数がより多い色を返す
    def getWinner(self) -> Disc:
        pass

    # 黒石と白石の数を返す
    def getDiscNum(self) -> tuple:
        pass

    # 指定された場所の石の色を返す
    def getLocationDisc(self, location:Location) -> Disc:
        pass

    # ゲームの終了判定
    def gameIsFinished(self) -> bool:
        pass
