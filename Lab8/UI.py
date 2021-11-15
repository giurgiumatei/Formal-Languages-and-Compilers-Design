
from Grammar import Grammar


class UI:

    def __init__(self) -> None:
        self.grammar = Grammar()
    
    def run(self):
        while True:
            print(">>")
            cmd = input()

            if cmd == "1":
                self.read_grammar()
            if cmd == "2":
                self.print_production_for_non_terminal()


    def read_grammar(self):
        self.grammar.read_from_file('G1.txt')
        print(self.grammar)

    def print_production_for_non_terminal(self):
        print("Give ")

        non_terminal = input()
        print(self.grammar.get_productions_for_nonterminal(non_terminal))

