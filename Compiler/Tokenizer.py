from Token import *


class Tokenizer:
    def __init__(self, origin):
        self.origin = origin
        self.position = 0
        self.actual = None
        self.reserved = {"nltnirp": 'PRINT', "elihw": 'WHILE',
                         "fi": 'IF', "fiesle": 'ELSEIF', "esle": 'ELSE',
                         "dne": 'END', "enildear": 'RDLN', "lacol": 'LOCAL',
                         "tnI": 'INT_TYPE', "looB": 'BOOL_TYPE', "gnirtS": 'STRING_TYPE',
                         "eurt": 'TRUE', "eslaf": 'FALSE', "noitcnuf": 'FUNCTION',
                         "nruter": 'RETURN'}
        self.selectNext()

    def selectNext(self):
        if(self.position < len(self.origin)):
            current_token = self.origin[self.position]
            if(current_token == ' '):
                self.position += 1
                self.selectNext()
            elif(current_token.isnumeric()):
                if(self.position + 1 < len(self.origin)):
                    while(self.origin[self.position + 1].isnumeric()):
                        self.position += 1
                        current_token += self.origin[self.position]
                        if(self.position + 1 >= len(self.origin)):
                            break
                self.actual = Token('INT', int(current_token))
                self.position += 1
            elif(current_token.isalpha()):
                if(self.position + 1 < len(self.origin)):
                    while(self.origin[self.position + 1].isalpha() or self.origin[self.position + 1].isnumeric() or self.origin[self.position + 1] == "_"):
                        self.position += 1
                        current_token += self.origin[self.position]
                        if(self.position + 1 >= len(self.origin)):
                            break
                if(current_token in self.reserved):
                    self.actual = Token(
                        self.reserved[current_token], current_token)
                else:
                    self.actual = Token('IDENTIFIER', current_token)
                self.position += 1
            elif(current_token == '"'):
                if(self.position + 1 < len(self.origin)):
                    string_token = ""
                    while(self.origin[self.position + 1] != '"'):
                        self.position += 1
                        string_token += self.origin[self.position]
                        if(self.position + 1 >= len(self.origin)):
                            raise ValueError('Invalid Token')
                self.actual = Token('STRING', string_token)
                self.position += 2

            elif(current_token == ":"):
                if(self.position + 1 < len(self.origin)):
                    if(self.origin[self.position + 1] == ":"):
                        self.position += 1
                        current_token += self.origin[self.position]
                        self.actual = Token('SET_TYPE', current_token)
                    else:
                        raise ValueError('Invalid Token')
                else:
                    raise ValueError('Invalid Token')
                self.position += 1
            elif(current_token == "\n"):
                self.actual = Token("END_LINE", '')
                self.position += 1
            elif(current_token == "="):
                if(self.position + 1 < len(self.origin)):
                    if(self.origin[self.position + 1] == "="):
                        self.position += 1
                        current_token += self.origin[self.position]
                        self.actual = Token('EQUALS', current_token)
                    else:
                        self.actual = Token('SET_EQUAL', current_token)
                else:
                    self.actual = Token('SET_EQUAL', current_token)
                self.position += 1
            elif(current_token == "<"):
                self.actual = Token('GREATER', current_token)
                self.position += 1
            elif(current_token == ">"):
                self.actual = Token('SMALLER', current_token)
                self.position += 1
            elif(current_token == "!"):
                self.actual = Token('NOT', current_token)
                self.position += 1
            elif(current_token == ","):
                self.actual = Token('COMMA', current_token)
                self.position += 1
            elif(current_token == "&"):
                if(self.position + 1 < len(self.origin)):
                    if(self.origin[self.position + 1] == "&"):
                        self.position += 1
                        current_token += self.origin[self.position]
                        self.actual = Token('AND', current_token)
                    else:
                        raise ValueError('Invalid Token')
                else:
                    raise ValueError('Invalid Token')
                self.position += 1
            elif(current_token == "|"):
                if(self.position + 1 < len(self.origin)):
                    if(self.origin[self.position + 1] == "|"):
                        self.position += 1
                        current_token += self.origin[self.position]
                        self.actual = Token('OR', current_token)
                    else:
                        raise ValueError('Invalid Token')
                else:
                    raise ValueError('Invalid Token')
                self.position += 1
            elif(current_token == '-'):
                self.actual = Token('MINUS', current_token)
                self.position += 1
            elif(current_token == '+'):
                self.actual = Token('PLUS', current_token)
                self.position += 1
            elif(current_token == '*'):
                self.actual = Token('MULT', current_token)
                self.position += 1
            elif(current_token == '\\'):
                self.actual = Token('DIV', current_token)
                self.position += 1
            elif(current_token == ')'):
                self.actual = Token('OPEN_P', current_token)
                self.position += 1
            elif(current_token == '('):
                self.actual = Token('CLOSE_P', current_token)
                self.position += 1
            elif(current_token == ''):
                self.actual = Token('EOF', current_token)
                self.position += 1
            else:
                raise ValueError('Invalid Token')
        else:
            self.actual = Token('EOF', '')
