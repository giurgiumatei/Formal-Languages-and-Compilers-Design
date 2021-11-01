from __future__ import annotations


class FiniteAutomata:

    def __init__(self, set_of_all_states, set_of_input_symbols, initial_state, set_of_final_states, transitions):
        self.q = set_of_all_states
        self.e = set_of_input_symbols
        self.q0 = initial_state
        self.f = set_of_final_states
        self.s = transitions

    def is_dfa(self) -> bool:
        for key in self.s.keys():
            if len(self.s[key]) > 1:
                return False
        return True

    @staticmethod
    def get_line(line) -> str:
        return line.strip().split(' ')[2:]

    @staticmethod
    def process_file(file_name) -> FiniteAutomata:
        with open(file_name) as file:
            q = FiniteAutomata.get_line(file.readline())
            e = FiniteAutomata.get_line(file.readline())
            q0 = FiniteAutomata.get_line(file.readline())[0]
            f = FiniteAutomata.get_line(file.readline())

            s = {}
            file.readline()
            for line in file:
                source_state = line.strip().split('->')[0].strip().replace('(', '').replace(')', '').split(',')[0]
                value = line.strip().split('->')[0].strip().replace('(', '').replace(')', '').split(',')[1]
                destination_state = line.strip().split('->')[1].strip()

                if (source_state, value) in s.keys():
                    s[(source_state, value)].append(destination_state)
                else:
                    s[(source_state, value)] = [destination_state]

            return FiniteAutomata(q, e, q0, f, s)
