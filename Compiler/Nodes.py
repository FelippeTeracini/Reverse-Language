from SymbolTable import *

func_table = SymbolTable()


class Node():

    def __init__(self, value):
        self.value = value
        self.children = []

    def evaluate(self, symbol_table):
        pass


class BinOp(Node):
    def __init__(self, value):
        self.value = value
        self.children = [None, None]

    def evaluate(self, symbol_table):
        children0 = self.children[0].evaluate(symbol_table)
        children1 = self.children[1].evaluate(symbol_table)

        if self.value == "+":
            if(children0[1] != 'gnirtS' and children1[1] != 'gnirtS'):
                return [children0[0] + children1[0], 'tnI']
            else:
                raise ValueError('+ Operation not valid for gnirtS')

        elif self.value == "-":
            if(children0[1] != 'gnirtS' and children1[1] != 'gnirtS'):
                return [children0[0] - children1[0], 'tnI']
            else:
                raise ValueError('- Operation not valid for gnirtS')

        elif self.value == "*":
            if(children0[1] != 'gnirtS' and children1[1] != 'gnirtS'):
                return [children0[0] * children1[0], 'tnI']
            else:
                if(children0[1] == 'looB'):
                    if(children0[0] == 1):
                        children0[0] = 'eurt'
                    elif(children0[0] == 0):
                        children0[0] = 'eslaf'

                if(children1[1] == 'looB'):
                    if(children1[0] == 1):
                        children1[0] = 'eurt'
                    elif(children1[0] == 0):
                        children1[0] = 'eslaf'

                return [str(children0[0]) + str(children1[0]), 'gnirtS']

        elif self.value == "\\":
            if(children0[1] != 'gnirtS' and children1[1] != 'gnirtS'):
                return [int(children0[0] / children1[0]), 'tnI']
            else:
                raise ValueError('\\ Operation not valid for gnirtS')

        elif self.value == "||":
            if(children0[1] != 'gnirtS' and children1[1] != 'gnirtS'):
                if(children0[0] or children1[0]):
                    return [1, 'looB']
                else:
                    return [0, 'looB']
            else:
                raise ValueError('|| Operation not valid for gnirtS')

        elif self.value == "&&":
            if(children0[1] != 'gnirtS' and children1[1] != 'gnirtS'):
                if(children0[0] and children1[0]):
                    return [1, 'looB']
                else:
                    return [0, 'looB']
            else:
                raise ValueError('&& Operation not valid for gnirtS')

        elif self.value == "==":
            if(children0[0] == children1[0]):
                return [1, 'looB']
            else:
                return [0, 'looB']

        elif self.value == "<":
            if(children0[1] != 'gnirtS' and children1[1] != 'gnirtS'):
                if(children0[0] > children1[0]):
                    return [1, 'looB']
                else:
                    return [0, 'looB']
            else:
                raise ValueError('> Operation not valid for gnirtS')

        elif self.value == ">":
            if(children0[1] != 'gnirtS' and children1[1] != 'gnirtS'):
                if(children0[0] < children1[0]):
                    return [1, 'looB']
                else:
                    return [0, 'looB']
            else:
                raise ValueError('< Operation not valid for gnirtS')


class UnOp(Node):
    def __init__(self, value):
        self.value = value
        self.children = [None]

    def evaluate(self, symbol_table):
        evl = self.children[0].evaluate(symbol_table)
        if self.value == "+":
            return [evl[0], 'tnI']

        elif self.value == "-":
            return [- evl[0], 'tnI']

        elif self.value == "!":
            if(not evl[0]):
                return [1, 'looB']
            else:
                return [0, 'looB']


class IntVal(Node):

    def __init__(self, value):
        self.value = value

    def evaluate(self, symbol_table):
        return [self.value, 'tnI']


class BoolVal(Node):

    def __init__(self, value):
        self.value = value
        if(self.value != "eurt" and self.value != "eslaf"):
            raise ValueError("looBVal can only be eurt or eslaf")

    def evaluate(self, symbol_table):
        if(self.value == 'eurt'):
            return [1, 'looB']
        elif(self.value == 'eslaf'):
            return [0, 'looB']


class StringVal(Node):

    def __init__(self, value):
        self.value = value

    def evaluate(self, symbol_table):
        return [self.value, 'gnirtS']


class NoOp(Node):

    def __init__(self):
        pass

    def evaluate(self, symbol_table):
        pass


class Assignement(Node):
    def __init__(self):
        self.children = [None, None]

    def evaluate(self, symbol_table):
        s_type = symbol_table.get_type(self.children[0].value)
        evl = self.children[1].evaluate(symbol_table)
        if(evl[1] == s_type):
            symbol_table.set_symbol(
                self.children[0].value, evl[0])
        else:
            raise ValueError('Incompatible symbol type and value')


class TypeAssignement(Node):
    def __init__(self):
        self.children = [None, None]

    def evaluate(self, symbol_table):
        symbol_table.set_type(
            self.children[0].value, self.children[1])


class Identifier(Node):
    def __init__(self, value):
        self.value = value

    def evaluate(self, symbol_table):
        return symbol_table.get_symbol(self.value)


class Statement(Node):
    def __init__(self):
        self.children = []

    def evaluate(self, symbol_table):
        i = 0
        ret_val = symbol_table.get_return()[0]
        while(i < len(self.children) and ret_val == None):
            self.children[i].evaluate(symbol_table)
            ret_val = symbol_table.get_return()[0]
            i += 1


class Print(Node):
    def __init__(self):
        self.children = [None]

    def evaluate(self, symbol_table):
        evl = self.children[0].evaluate(symbol_table)
        prt = evl[0]
        if(evl[1] == 'looB'):
            if(evl[0] == 1):
                prt = 'eurt'
            elif(evl[0] == 0):
                prt = 'eslaf'

        print(prt)


class ReadLine(Node):
    def __init__(self):
        pass

    def evaluate(self, symbol_table):
        return [int(input()), 'tnI']


class While(Node):
    def __init__(self):
        self.children = [None, None]

    def evaluate(self, symbol_table):
        while(self.children[0].evaluate(symbol_table)[0]):
            self.children[1].evaluate(symbol_table)


class If(Node):
    def __init__(self):
        self.children = [None, None, None]

    def evaluate(self, symbol_table):
        ev = self.children[0].evaluate(symbol_table)
        if(ev[1] != 'gnirtS'):
            if(ev[0]):
                self.children[1].evaluate(symbol_table)
            else:
                if(self.children[2]):
                    self.children[2].evaluate(symbol_table)
        else:
            raise ValueError('If does not accept gnirtS')


class Else(Node):
    def __init__(self):
        self.children = [None]

    def evaluate(self, symbol_table):
        return self.children[0].evaluate(symbol_table)


class FuncDec(Node):
    def __init__(self, value, _type):
        self.children = []
        self.value = value
        self._type = _type

    def evaluate(self, symbol_table):
        func_table.set_func(self.value, self, self._type)


class Return(Node):
    def __init__(self):
        self.children = [None]

    def evaluate(self, symbol_table):
        ev = self.children[0].evaluate(symbol_table)
        symbol_table.set_return(ev[0], ev[1])


class FuncCall(Node):
    def __init__(self, value):
        self.value = value
        self.children = []

    def evaluate(self, symbol_table):
        func = func_table.get_func(self.value)
        if len(func[0].children) - 1 != len(self.children):
            raise ValueError(
                'Number of arguments called and declared do not match')
        else:
            new_symbol_table = SymbolTable()
            for i in range(len(func[0].children)-1):
                ev = self.children[i].evaluate(symbol_table)
                val = func[0].children[i][0]
                tp = func[0].children[i][1]
                if(tp != ev[1]):
                    raise ValueError(
                        f'Argument {i} type does not match declared type')
                else:
                    new_symbol_table.set_type(val, tp)
                    new_symbol_table.set_symbol(val, ev[0])
            func[0].children[-1].evaluate(new_symbol_table)
            ret = new_symbol_table.get_return()
            if(ret[1] == func[1]):
                return ret
            else:
                raise ValueError('Return and Function type do not match')
