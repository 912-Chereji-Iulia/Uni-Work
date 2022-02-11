from domain.board import Board
from strategy.Strategy import Strategy
from ui.GUI import GUI
from ui.UI import UI

done = False
while not done:
    try:
        inp = input("UI or GUI? >>> ")
        game = Strategy(Board())
        if inp.lower() == 'ui':
            done=True
            ui = UI(game)
            ui.start()
        elif inp.lower() == 'gui':
            done = True
            ui = GUI(game)
        else:
            raise ValueError
    except ValueError:
        print("Bad input")