from Domain.SymbolTable import SymbolTable

symbol_table = SymbolTable(17)

symbol_table.add('a')
symbol_table.add('b')
symbol_table.add('1')
symbol_table.add('ab')
symbol_table.add('ba')


#print(symbol_table)

assert (symbol_table.contains('a') is True)
assert (symbol_table.contains('b') is True)
assert (symbol_table.contains('1') is True)
assert (symbol_table.get_position('ab') == (14, 0))
assert (symbol_table.get_position('ba') == (14, 1))

print("All tests passing")
