import os

from Location.Location import Location
from Board.BitBoard import BitBoard
from Board.Disc import Disc
import Solver.Human
import Solver.Random
import Solver.PrimitiveMonteCarloMethod
import Solver.StaticEval_Alphabeta

class Game:

    # ゲームの実行
    def play(self, firstSolverName:str="Human", secondSolverName:str="Human") -> None:
        self.board = BitBoard()
        # 先手、後手のソルバーのオブジェクト生成
        self.firstSolver = self.generateSolver(firstSolverName)
        self.secondSolver = self.generateSolver(secondSolverName)

        self.display()
        while True:
            # 1人目の手番
            location = self.firstSolver.selectLocation(self.board)
            if location == "pass":
                self.board.passPut()
            else:
                self.board.put(location)

            if self.board.gameIsFinished():
                break
            self.board.updateBoardStatus()
            self.display()

            # 2人目の手番
            location = self.secondSolver.selectLocation(self.board)
            if location == "pass":
                self.board.passPut()
            else:
                self.board.put(location)
                
            if self.board.gameIsFinished():
                break
            self.board.updateBoardStatus()
            self.display()

        self.displayResult()

    # プレイヤーのオブジェクトを生成
    def generateSolver(self, name:str) -> object:
        if name == "Human":
            solver = Solver.Human.Human()
        elif name == "Random":
            solver = Solver.Random.Random()
        elif name == "PMCM":
            solver = Solver.PrimitiveMonteCarloMethod.PrimitiveMonteCarloMethod(samplingNum=100)
        elif name == "StaticEval_Alphabeta":
            solver = Solver.StaticEval_Alphabeta.StaticEval_Alphabeta(depth=5)
        else:
            # デフォルトでは人間が打つ
            solver = Solver.Human.Human()

        return solver

    # ゲームの描画
    def display(self) -> None:
        if type(self.board) is BitBoard:
            self._displayBitBoard()
        print(f"turn : {self.board.turn}")
        if self.board.player == Disc.black:
            print("black`s turn")
        elif self.board.player == Disc.white:
            print("white`s turn")

    # BitBoardの描画
    def _displayBitBoard(self) -> None:
        os.system("cls")

        print(" ", end="")
        for i in range(1, 9):
            print(i, end="")
        print()
        for i in range(1, 9):
            print(i, end="")
            for j in range(1, 9):
                loc = Location(i, j)
                if self.board.turn%2 == 1:
                    # 奇数ターンならplayerBoardは先手(黒)のボード
                    if (self.board.locationToBits(loc) & self.board.playerBoard) != 0:
                        print("b", end="")
                    elif (self.board.locationToBits(loc) & self.board.opponentBoard) != 0:
                        print("w", end="")
                    else:
                        print(" ", end="")
                else:
                    # 偶数ターンならplayerBoardは後手(白)のボード
                    if (self.board.locationToBits(loc) & self.board.playerBoard) != 0:
                        print("w", end="")
                    elif (self.board.locationToBits(loc) & self.board.opponentBoard) != 0:
                        print("b", end="")
                    else:
                        print(" ", end="")
            print()
        print()

    # ゲームの結果を表示
    def displayResult(self):
        self.display()
        winner = self.board.getWinner()
        blackDiscNum, whiteDiscNum = self.board.getDiscNum()

        print(f"black : {blackDiscNum}  white : {whiteDiscNum}")
        if winner == Disc.black:
            print("winner : black")
        elif winner == Disc.white:
            print("winner : white")
        else:
            print("draw")
