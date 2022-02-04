
# 盤上の場所を表すクラス
class Location:
    def __init__(self, row:int=-1, column:int=-1) -> None:
        self.row = row
        self.column = column

    # 範囲の検証
    def checkRange(self) -> bool:
        if (1 <= self.row <= 8) and (1 <= self.column <= 8):
            return True
        else:
            return False
