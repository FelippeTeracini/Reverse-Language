import sys
from Parser import *
from PrePro import *
from SymbolTable import *

symbol_table = SymbolTable()


file = open(sys.argv[1], "r")
code = file.read()
code = PrePro().filter(code)
ast = Parser.run(code)
ast.evaluate(symbol_table)
