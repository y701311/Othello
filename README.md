# Othello

これは単純なオセロゲームです。

あなたは自分だけのオセロAIを簡単に作り出すことが出来ます。

1. Solverフォルダの下に自分のオセロAIを作る
    - 既にある盤面評価関数や探索法を利用することが出来ます
    - Solver/Solver.pyのSolverクラスを継承し、メソッドselectLocationを記述してください
    - 盤面評価関数を追加する場合は、Solver/EvaluationFunction/EvaluationFunction.pyのEvaluationFunctionクラスを継承し、メソッドevaluateを記述してください
2. Game/Game.pyにオセロAIの名前を登録する
    - Game/Game.pyにオセロAIをimportし、名前を指定するとあなたのオセロAIが生成されるようにgenerateSolverへ変更を加えます

    ```python:Game/Game.py
    def generateSolver(self, name:str) -> object:
        if name == "Human":
            solver = Solver.Human.Human()
        elif name == "Random":
            solver = Solver.Random.Random()
        elif name == "" # add your AI`s name!
            solver = Solver.Hoge.Hoge()
    ```

3. main.pyのmainにてあなたのオセロAIの名前を指定する
    - main.pyであなたのオセロAIを指定してゲームをしましょう！

    ```python:main.py
    # specify your AI` name, and choose your opponent
    game.play(firstSolverName="",secondSolverName="")
    ```
