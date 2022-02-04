from Board.Board import Board
from Location.Location import Location
from Board.Disc import Disc

# BoardクラスのbitBoardとしての実装
class BitBoard(Board):
    def __init__(self) -> None:
        # 打っているプレイヤーの色
        self.player = Disc.black
        self.turn = 1
        self.playerBoard = 0x0000000810000000
        self.opponentBoard = 0x0000001008000000
    
    # Locationで指定された場所のみビットが立っているボードに変換
    def locationToBits(self, location:Location) -> int:
        bits = 1
        shift = 63 - (8*(location.row - 1) + (location.column - 1))
        return bits << shift

    # 指定された場所に置く
    def put(self, location:Location) -> None:
        if self.canPut(location):
            put = self.locationToBits(location)
            self.reverse(put)

    # パスをする
    def passPut(self) -> None:
        pass

    # 指定された場所に置けるかどうか
    def canPut(self, location:Location) -> bool:
        if location.checkRenge():
            putBoard = self.locationToBits(location)
            legalBoard = self.makeLegalBoard()
            # 指定された場所が合法手に含まれているか
            return (putBoard & legalBoard) == putBoard
        else:
            return False

    # 合法手のビットのみが立っているボードを生成
    def makeLegalBoard(self) -> int:
        legalBoard = 0
        # 空きマスのみにビットが立っているボード
        blankBoard = ~(self.playerBoard | self.opponentBoard)
        # 左右の端を除く相手ボード
        horizontalMaskedOpponentBoard = self.opponentBoard & 0x7e7e7e7e7e7e7e7e
        # 上下の端を除く相手ボード
        verticalMaskedOpponentBoard = self.opponentBoard & 0x00ffffffffffff00
        # 上下左右の端を除く相手ボード
        allSideMaskedOpponentBoard = self.opponentBoard & 0x007e7e7e7e7e7e00
        # 相手の石がある場所を保存する
        opponentDiscs = 0

        # 8方向をチェック
        # 1度に返せる石は6つまで
        # 左
        opponentDiscs = horizontalMaskedOpponentBoard & (self.playerBoard << 1)
        opponentDiscs |= horizontalMaskedOpponentBoard & (opponentDiscs << 1)
        opponentDiscs |= horizontalMaskedOpponentBoard & (opponentDiscs << 1)
        opponentDiscs |= horizontalMaskedOpponentBoard & (opponentDiscs << 1)
        opponentDiscs |= horizontalMaskedOpponentBoard & (opponentDiscs << 1)
        opponentDiscs |= horizontalMaskedOpponentBoard & (opponentDiscs << 1)
        legalBoard |= blankBoard & (opponentDiscs << 1)

        # 右
        opponentDiscs = horizontalMaskedOpponentBoard & (self.playerBoard >> 1)
        opponentDiscs |= horizontalMaskedOpponentBoard & (opponentDiscs >> 1)
        opponentDiscs |= horizontalMaskedOpponentBoard & (opponentDiscs >> 1)
        opponentDiscs |= horizontalMaskedOpponentBoard & (opponentDiscs >> 1)
        opponentDiscs |= horizontalMaskedOpponentBoard & (opponentDiscs >> 1)
        opponentDiscs |= horizontalMaskedOpponentBoard & (opponentDiscs >> 1)
        legalBoard |= blankBoard & (opponentDiscs >> 1)

        # 上
        opponentDiscs = verticalMaskedOpponentBoard & (self.playerBoard << 8)
        opponentDiscs |= verticalMaskedOpponentBoard & (opponentDiscs << 8)
        opponentDiscs |= verticalMaskedOpponentBoard & (opponentDiscs << 8)
        opponentDiscs |= verticalMaskedOpponentBoard & (opponentDiscs << 8)
        opponentDiscs |= verticalMaskedOpponentBoard & (opponentDiscs << 8)
        opponentDiscs |= verticalMaskedOpponentBoard & (opponentDiscs << 8)
        legalBoard |= blankBoard & (opponentDiscs << 8)

        # 下
        opponentDiscs = verticalMaskedOpponentBoard & (self.playerBoard >> 8)
        opponentDiscs |= verticalMaskedOpponentBoard & (opponentDiscs >> 8)
        opponentDiscs |= verticalMaskedOpponentBoard & (opponentDiscs >> 8)
        opponentDiscs |= verticalMaskedOpponentBoard & (opponentDiscs >> 8)
        opponentDiscs |= verticalMaskedOpponentBoard & (opponentDiscs >> 8)
        opponentDiscs |= verticalMaskedOpponentBoard & (opponentDiscs >> 8)
        legalBoard |= blankBoard & (opponentDiscs >> 8)

        # 左上
        opponentDiscs = allSideMaskedOpponentBoard & (self.playerBoard << 9)
        opponentDiscs |= allSideMaskedOpponentBoard & (opponentDiscs << 9)
        opponentDiscs |= allSideMaskedOpponentBoard & (opponentDiscs << 9)
        opponentDiscs |= allSideMaskedOpponentBoard & (opponentDiscs << 9)
        opponentDiscs |= allSideMaskedOpponentBoard & (opponentDiscs << 9)
        opponentDiscs |= allSideMaskedOpponentBoard & (opponentDiscs << 9)
        legalBoard |= blankBoard & (opponentDiscs << 9)

        # 右上
        opponentDiscs = allSideMaskedOpponentBoard & (self.playerBoard << 7)
        opponentDiscs |= allSideMaskedOpponentBoard & (opponentDiscs << 7)
        opponentDiscs |= allSideMaskedOpponentBoard & (opponentDiscs << 7)
        opponentDiscs |= allSideMaskedOpponentBoard & (opponentDiscs << 7)
        opponentDiscs |= allSideMaskedOpponentBoard & (opponentDiscs << 7)
        opponentDiscs |= allSideMaskedOpponentBoard & (opponentDiscs << 7)
        legalBoard |= blankBoard & (opponentDiscs << 7)

        # 右下
        opponentDiscs = allSideMaskedOpponentBoard & (self.playerBoard >> 9)
        opponentDiscs |= allSideMaskedOpponentBoard & (opponentDiscs >> 9)
        opponentDiscs |= allSideMaskedOpponentBoard & (opponentDiscs >> 9)
        opponentDiscs |= allSideMaskedOpponentBoard & (opponentDiscs >> 9)
        opponentDiscs |= allSideMaskedOpponentBoard & (opponentDiscs >> 9)
        opponentDiscs |= allSideMaskedOpponentBoard & (opponentDiscs >> 9)
        legalBoard |= blankBoard & (opponentDiscs >> 9)
        
        # 左下
        opponentDiscs = allSideMaskedOpponentBoard & (self.playerBoard >> 7)
        opponentDiscs |= allSideMaskedOpponentBoard & (opponentDiscs >> 7)
        opponentDiscs |= allSideMaskedOpponentBoard & (opponentDiscs >> 7)
        opponentDiscs |= allSideMaskedOpponentBoard & (opponentDiscs >> 7)
        opponentDiscs |= allSideMaskedOpponentBoard & (opponentDiscs >> 7)
        opponentDiscs |= allSideMaskedOpponentBoard & (opponentDiscs >> 7)
        legalBoard |= blankBoard & (opponentDiscs >> 7)

        return legalBoard

    # 置ける場所をLocationのlistとして返す
    def getPlaceableLocation(self) -> list:
        placeableLocation = []
        legalBoard = self.makeLegalBoard()
        mask = 1

        for i in range(1, 9):
            for j in range(1, 9):
                if (legalBoard & (mask << (63 - (8*(i - 1) + (j - 1))))) != 0:
                    placeableLocation.append(Location(i, j))
        
        return placeableLocation

    # 反転処理
    def reverse(self, put:int) -> None:
        rev = self.getReverseBoard(put)

        self.playerBoard ^= (put | rev)
        self.opponentBoard ^= rev

    # 反転箇所のビットが立っているボードを返却
    def getReverseBoard(self, put:int) -> int:
        # 反転箇所のビットが立っているボード
        rev = 0

        # 左右の端を除く相手ボード
        horizontalMaskedOpponentBoard = self.opponentBoard & 0x7e7e7e7e7e7e7e7e
        # 上下の端を除く相手ボード
        verticalMaskedOpponentBoard = self.opponentBoard & 0x00ffffffffffff00
        # 上下左右の端を除く相手ボード
        allSideMaskedOpponentBoard = self.opponentBoard & 0x007e7e7e7e7e7e00

        # 8方向をチェック
        # 1度に返せる石は6つまで
        # 左
        opponentDiscs = horizontalMaskedOpponentBoard & (put << 1)
        opponentDiscs |= horizontalMaskedOpponentBoard & (opponentDiscs << 1)
        opponentDiscs |= horizontalMaskedOpponentBoard & (opponentDiscs << 1)
        opponentDiscs |= horizontalMaskedOpponentBoard & (opponentDiscs << 1)
        opponentDiscs |= horizontalMaskedOpponentBoard & (opponentDiscs << 1)
        opponentDiscs |= horizontalMaskedOpponentBoard & (opponentDiscs << 1)
        if (self.playerBoard & (opponentDiscs << 1)) != 0:
            rev |= opponentDiscs

        # 右
        opponentDiscs = horizontalMaskedOpponentBoard & (put >> 1)
        opponentDiscs |= horizontalMaskedOpponentBoard & (opponentDiscs >> 1)
        opponentDiscs |= horizontalMaskedOpponentBoard & (opponentDiscs >> 1)
        opponentDiscs |= horizontalMaskedOpponentBoard & (opponentDiscs >> 1)
        opponentDiscs |= horizontalMaskedOpponentBoard & (opponentDiscs >> 1)
        opponentDiscs |= horizontalMaskedOpponentBoard & (opponentDiscs >> 1)
        if (self.playerBoard & (opponentDiscs >> 1)) != 0:
            rev |= opponentDiscs

        # 上
        opponentDiscs = verticalMaskedOpponentBoard & (put << 8)
        opponentDiscs |= verticalMaskedOpponentBoard & (opponentDiscs << 8)
        opponentDiscs |= verticalMaskedOpponentBoard & (opponentDiscs << 8)
        opponentDiscs |= verticalMaskedOpponentBoard & (opponentDiscs << 8)
        opponentDiscs |= verticalMaskedOpponentBoard & (opponentDiscs << 8)
        opponentDiscs |= verticalMaskedOpponentBoard & (opponentDiscs << 8)
        if (self.playerBoard & (opponentDiscs << 8)) != 0:
            rev |= opponentDiscs

        # 下
        opponentDiscs = verticalMaskedOpponentBoard & (put >> 8)
        opponentDiscs |= verticalMaskedOpponentBoard & (opponentDiscs >> 8)
        opponentDiscs |= verticalMaskedOpponentBoard & (opponentDiscs >> 8)
        opponentDiscs |= verticalMaskedOpponentBoard & (opponentDiscs >> 8)
        opponentDiscs |= verticalMaskedOpponentBoard & (opponentDiscs >> 8)
        opponentDiscs |= verticalMaskedOpponentBoard & (opponentDiscs >> 8)
        if (self.playerBoard & (opponentDiscs >> 8)) != 0:
            rev |= opponentDiscs

        # 左上
        opponentDiscs = allSideMaskedOpponentBoard & (put << 9)
        opponentDiscs |= allSideMaskedOpponentBoard & (opponentDiscs << 9)
        opponentDiscs |= allSideMaskedOpponentBoard & (opponentDiscs << 9)
        opponentDiscs |= allSideMaskedOpponentBoard & (opponentDiscs << 9)
        opponentDiscs |= allSideMaskedOpponentBoard & (opponentDiscs << 9)
        opponentDiscs |= allSideMaskedOpponentBoard & (opponentDiscs << 9)
        if (self.playerBoard & (opponentDiscs << 9)) != 0:
            rev |= opponentDiscs

        # 右上
        opponentDiscs = allSideMaskedOpponentBoard & (put << 7)
        opponentDiscs |= allSideMaskedOpponentBoard & (opponentDiscs << 7)
        opponentDiscs |= allSideMaskedOpponentBoard & (opponentDiscs << 7)
        opponentDiscs |= allSideMaskedOpponentBoard & (opponentDiscs << 7)
        opponentDiscs |= allSideMaskedOpponentBoard & (opponentDiscs << 7)
        opponentDiscs |= allSideMaskedOpponentBoard & (opponentDiscs << 7)
        if (self.playerBoard & (opponentDiscs << 7)) != 0:
            rev |= opponentDiscs

        # 右下
        opponentDiscs = allSideMaskedOpponentBoard & (put >> 9)
        opponentDiscs |= allSideMaskedOpponentBoard & (opponentDiscs >> 9)
        opponentDiscs |= allSideMaskedOpponentBoard & (opponentDiscs >> 9)
        opponentDiscs |= allSideMaskedOpponentBoard & (opponentDiscs >> 9)
        opponentDiscs |= allSideMaskedOpponentBoard & (opponentDiscs >> 9)
        opponentDiscs |= allSideMaskedOpponentBoard & (opponentDiscs >> 9)
        if (self.playerBoard & (opponentDiscs >> 9)) != 0:
            rev |= opponentDiscs
        
        # 左下
        opponentDiscs = allSideMaskedOpponentBoard & (put >> 7)
        opponentDiscs |= allSideMaskedOpponentBoard & (opponentDiscs >> 7)
        opponentDiscs |= allSideMaskedOpponentBoard & (opponentDiscs >> 7)
        opponentDiscs |= allSideMaskedOpponentBoard & (opponentDiscs >> 7)
        opponentDiscs |= allSideMaskedOpponentBoard & (opponentDiscs >> 7)
        opponentDiscs |= allSideMaskedOpponentBoard & (opponentDiscs >> 7)
        if (self.playerBoard & (opponentDiscs >> 7)) != 0:
            rev |= opponentDiscs

        return rev

    # ゲームの終了判定
    def gameIsFinished(self) -> bool:
        # 自分、相手が共に合法手が無いなら終了
        playerLegalBoard = self.makeLegalBoard()
        self.swapBoard()
        opponentLegalBoard = self.makeLegalBoard()
        self.swapBoard()

        return (playerLegalBoard == 0) and (opponentLegalBoard == 0)

    # ボードのパラメータを更新
    def updateBoardStatus(self):
        self.swapBoard()
        self.changePlayerColor()
        self.turn += 1

    # 自分と相手のボードを入れ替える
    def swapBoard(self) -> None:
        temp = self.playerBoard
        self.playerBoard = self.opponentBoard
        self.opponentBoard = temp

    # 打ち手の色を入れ替える
    def changePlayerColor(self) -> None:
        if self.player == Disc.black:
            self.player = Disc.white
        else:
            self.player = Disc.black

    # 石の数がより多い色を返す
    def getWinner(self) -> Disc:
        blackDiscNum, whiteDiscNum = self.getDiscNum()
        
        if blackDiscNum > whiteDiscNum:
            return Disc.black
        elif blackDiscNum < whiteDiscNum:
            return Disc.white
        else:
            return Disc.empty

    # 黒石と白石の数を返す
    def getDiscNum(self) -> tuple:
        if self.player == Disc.black:
            blackDiscNum = self.numOfDisc(self.playerBoard)
            whiteDiscNum = self.numOfDisc(self.opponentBoard)
        else:
            whiteDiscNum = self.numOfDisc(self.playerBoard)
            blackDiscNum = self.numOfDisc(self.opponentBoard)
        
        return blackDiscNum, whiteDiscNum

    # ボードの立っているビット数を数える
    def numOfDisc(self, board:int) -> int:
        # forで回してもいいが、ビット演算で計算すると
        # O(N)からO(logN)になる
        mask1bit = 0x5555555555555555
        mask2bit = 0x3333333333333333
        mask4bit = 0x0f0f0f0f0f0f0f0f
        mask8bit = 0x00ff00ff00ff00ff
        mask16bit = 0x0000ffff0000ffff
        mask32bit = 0x00000000ffffffff

        board = (board & mask1bit) + ((board >> 1) & mask1bit)
        board = (board & mask2bit) + ((board >> 2) & mask2bit)
        board = (board & mask4bit) + ((board >> 4) & mask4bit)
        board = (board & mask8bit) + ((board >> 8) & mask8bit)
        board = (board & mask16bit) + ((board >> 16) & mask16bit)
        return (board & mask32bit) + ((board >> 32) & mask32bit)

    # 指定された場所の石の色を返す
    def getLocationDisc(self, location:Location) -> Disc:
        mask = self.locationToBits(location)
        if self.player == Disc.black:
            if (self.playerBoard & mask) != 0:
                return Disc.black
            elif (self.opponentBoard & mask) != 0:
                return Disc.white
            else:
                return Disc.empty
        elif self.player == Disc.white:
            if (self.playerBoard & mask) != 0:
                return Disc.white
            elif (self.opponentBoard & mask) != 0:
                return Disc.black
            else:
                return Disc.empty
