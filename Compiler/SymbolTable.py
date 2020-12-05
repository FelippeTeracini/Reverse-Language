class SymbolTable:

    def __init__(self):
        self.symbol_table = {'return': [None, None]}
        self.func_table = {}

    def set_symbol(self, symbol, symbol_value):
        if symbol in self.symbol_table.keys():
            self.symbol_table[symbol][0] = symbol_value
        else:
            raise ValueError(f'Symbol {symbol} not defined')

    def get_symbol(self, symbol):
        if symbol in self.symbol_table.keys():
            if(self.symbol_table[symbol][0] is not None):
                return self.symbol_table[symbol]
            else:
                raise ValueError(f'Symbol {symbol} has no value')
        else:
            raise ValueError(f'Symbol {symbol} not in symbol table')

    def set_type(self, symbol, symbol_type):
        if(symbol not in self.func_table.keys() and symbol not in self.symbol_table.keys()):
            self.symbol_table[symbol] = [None, symbol_type]
        else:
            raise ValueError(f'Symbol {symbol} already in symbol/func table')

    def get_type(self, symbol):
        if symbol in self.symbol_table.keys():
            return self.symbol_table[symbol][1]
        else:
            raise ValueError(f'Symbol {symbol} not in symbol table')

    def set_func(self, func_symbol, func, _type):
        if(func_symbol not in self.func_table.keys() and func_symbol not in self.symbol_table.keys()):
            self.func_table[func_symbol] = [func, _type]
        else:
            raise ValueError(
                f'Func Symbol {func_symbol} already in symbol/func table')

    def get_func(self, func_symbol):
        if(func_symbol in self.func_table.keys()):
            return self.func_table[func_symbol]
        else:
            raise ValueError(f'Func Symbol {func_symbol} not in func table')

    def set_return(self, value, _type):
        self.symbol_table['return'] = [value, _type]

    def get_return(self):
        return self.symbol_table['return']
