from types import FunctionType
import numpy as np
from copy import deepcopy

from Board.Board import Board
from Board.Disc import Disc
from Location.Location import Location

# モンテカルロ木探索のためのノードを表すクラス
class Node:

    def __init__(self, board:Board, parentNode:"Node", location:Location) -> None:
        self.board = board
        self.parentNode = parentNode
        self.location = location

        self.win = 0
        self.visitNum = 0
        self.childNodes = []
        self.untriedLocations = board.getPlaceableLocation()

    # 子ノードを展開する
    def expandChild(self) -> "Node":
        board = deepcopy(self.board)
        if len(self.untriedLocations) != 0:
            loc = self.untriedLocations.pop(np.random.randint(len(self.untriedLocations)))
            board.put(loc)
            board.updateBoardStatus()
            child = Node(board, self, loc)
        else:
            board.passPut()
            board.updateBoardStatus()
            child = Node(board, self, None)

        self.childNodes.append(child)
        return child

    # ゲーム終了までランダムに石を置き、勝った石の色を返す
    def playout(self) -> Disc:
        board = deepcopy(self.board)

        while not board.gameIsFinished():
            placeableLocation = board.getPlaceableLocation()
            if len(placeableLocation) != 0:
                loc = placeableLocation[np.random.randint(len(placeableLocation))]
                board.put(loc)
            else:
                board.passPut()
            board.updateBoardStatus()
        
        return board.getWinner()

    # プレイアウトの結果を木の根まで伝播させる
    def backpropagation(self, winner:Disc) -> None:
        node = self
        while node is not None:
            node.visitNum += 1
            if winner == node.board.player:
                node.win += 1
            elif winner == Disc.empty:
                node.win += 0.5

            node = node.parentNode

    # 子ノードを選択する
    def selectChildNode(self, selectChildNodeAlgorithm:str, evaluationFunction:FunctionType):
        if selectChildNodeAlgorithm == "UTC":
            return self.selectChildNodeByUct()

    # UCB1に基づいて子ノードを選択する
    def selectChildNodeByUct(self) -> "Node":
        selectionPriority = []
        for child in self.childNodes:
            selectionPriority.append(self._calculatePriority(child))
        
        index = np.argmax(selectionPriority)
        return self.childNodes[index]

    # UCB1に基づいたノードの探索優先度を返す
    def _calculatePriority(self, node:"Node") -> float:
        c = np.sqrt(2)
        value = node.win / node.visitNum + c * np.sqrt(np.log(self.visitNum) / node.visitNum)
        return value
