from strategy.Strategy import Strategy


class UI:
    def __init__(self, strategy: Strategy):
        self._strategy = strategy
        self._start_comp = False
        self._turn = 1

    def start(self):
        done = False
        while not done:
            try:
                x = int(input("\033[94mGive the dimension of the board: \033[0m\nheight = "))
                y = int(input("width = "))
                if x < 1 or y < 1:
                    raise ValueError
                player = input("\033[94mDo you want to be the first player?\n\033[0m a)Yes  b)No\n")
                self._strategy.set_row(x)
                self._strategy.set_column(y)
                self._strategy.create_board()
                if player == 'a':
                    self._turn = 1
                    self._start_comp = False
                elif player == 'b':
                    self._turn = 2
                    self._start_comp = True
                while self._strategy.game_not_over() is True:
                    if self._turn == 1:
                        try:
                            print(str(self._strategy.get_board()))
                            x = int(input("x = "))
                            y = int(input("y = "))
                            self._strategy.player_move(x, y)
                            self._turn = 2
                        except Exception as ex:
                            print(str(ex))
                    elif self._turn == 2:
                        self._strategy.computer_move(self._start_comp, x, y)
                        self._turn = 1
                print(str(self._strategy.get_board()))
                if self._turn == 2:
                    print("\033[33mCongrats! You won!\033[0m")
                else:
                    print("\033[96mComputer has won! Try again!\033[0m")

                again = input("\n \033[94mDo you want to play again?\n\033[0m a) Yes  b) No\n")
                if again == 'a':
                    self._strategy.reset_board()
                elif again == 'b':
                    done = True
                    print("Bye bye!")
                else:
                    print("Invalid option!")
            except ValueError:
                print("Invalid coordinates!")