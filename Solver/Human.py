from Board.Board import Board
from Location.Location import Location
from Solver.Solver import Solver

# 人間のソルバー
class Human(Solver):
    
    # 石を置く場所を選択する
    def selectLocation(self, board:Board) -> Location:
        print("Please enter row and column. If you will pass, input \"pass\".")
        print("e.g. 53 is row=5, column=3")

        location = Location(-1, -1)
        while (not location.checkRange()) or (not board.canPut(location)):
            inputStr = input()
            if inputStr == "pass":
                return "pass"
            else:
                locationInput = int(inputStr)
                location.row = (locationInput // 10) % 10
                location.column = locationInput % 10
                if (not location.checkRange()) or (not board.canPut(location)):
                    print("Invalid input.")

        return location