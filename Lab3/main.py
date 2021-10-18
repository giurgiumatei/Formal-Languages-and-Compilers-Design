from Domain.ProgramInternalForm import ProgramInternalForm
from Domain.SymbolTable import SymbolTable
from Domain.Symbols import read_file



def main():
    separators, operators, reserved_words = read_file()
    symbol_table = SymbolTable(20)
    program_internal_form = ProgramInternalForm()


main()