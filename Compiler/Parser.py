from Tokenizer import *
from Nodes import *


class Parser:

    tokens = None

    @staticmethod
    def parseFactor():
        if(Parser.tokens.actual.token_type == 'INT'):
            result = IntVal(Parser.tokens.actual.token_value)
            Parser.tokens.selectNext()
            return result
        elif(Parser.tokens.actual.token_type == 'TRUE' or Parser.tokens.actual.token_type == 'FALSE'):
            result = BoolVal(Parser.tokens.actual.token_value)
            Parser.tokens.selectNext()
            return result
        elif(Parser.tokens.actual.token_type == 'STRING'):
            result = StringVal(Parser.tokens.actual.token_value)
            Parser.tokens.selectNext()
            return result
        elif(Parser.tokens.actual.token_type == 'IDENTIFIER'):
            ident = Parser.tokens.actual.token_value
            Parser.tokens.selectNext()
            if(Parser.tokens.actual.token_type == 'OPEN_P'):
                result = FuncCall(ident)
                Parser.tokens.selectNext()
                if(Parser.tokens.actual.token_type != 'CLOSE_P'):
                    result.children.append(Parser.parseRelEx())
                    while(Parser.tokens.actual.token_type == 'COMMA'):
                        Parser.tokens.selectNext()
                        result.children.append(Parser.parseRelEx())
                if(Parser.tokens.actual.token_type == 'CLOSE_P'):
                    Parser.tokens.selectNext()
                else:
                    raise ValueError(
                        'OPEN_P needs matching CLOSE_P (IDENTIFIER FACTOR)')
            else:
                result = Identifier(ident)
            return result
        elif(Parser.tokens.actual.token_type == 'PLUS' or Parser.tokens.actual.token_type == 'MINUS' or Parser.tokens.actual.token_type == 'NOT'):
            result = UnOp(Parser.tokens.actual.token_value)
            Parser.tokens.selectNext()
            result.children[0] = Parser.parseFactor()
            return result
        elif(Parser.tokens.actual.token_type == 'OPEN_P'):
            Parser.tokens.selectNext()
            result = Parser.parseRelEx()
            if(Parser.tokens.actual.token_type == 'CLOSE_P'):
                Parser.tokens.selectNext()
                return result
            else:
                raise ValueError('( must have a matching )')
        elif(Parser.tokens.actual.token_type == 'CLOSE_P'):
            raise ValueError(') can not come before a matching (')
        else:
            raise ValueError('Invalid token for FACTOR')

    @staticmethod
    def parseTerm():
        result = Parser.parseFactor()
        while(Parser.tokens.actual.token_type == 'MULT' or Parser.tokens.actual.token_type == 'DIV' or Parser.tokens.actual.token_type == 'AND'):
            if Parser.tokens.actual.token_type == 'MULT' or Parser.tokens.actual.token_type == 'DIV' or Parser.tokens.actual.token_type == 'AND':
                node = BinOp(Parser.tokens.actual.token_value)
                node.children[0] = result
                result = node
                Parser.tokens.selectNext()
                result.children[1] = Parser.parseFactor()
        return result

    @staticmethod
    def parseExpression():
        result = Parser.parseTerm()
        while(Parser.tokens.actual.token_type == 'PLUS' or Parser.tokens.actual.token_type == 'MINUS' or Parser.tokens.actual.token_type == 'OR'):
            if Parser.tokens.actual.token_type == 'PLUS' or Parser.tokens.actual.token_type == 'MINUS' or Parser.tokens.actual.token_type == 'OR':
                node = BinOp(Parser.tokens.actual.token_value)
                node.children[0] = result
                result = node
                Parser.tokens.selectNext()
                result.children[1] = Parser.parseTerm()
        return result

    @staticmethod
    def parseCommand():
        node = NoOp()
        if(Parser.tokens.actual.token_type == 'IDENTIFIER'):
            ident = Parser.tokens.actual.token_value
            Parser.tokens.selectNext()
            if(Parser.tokens.actual.token_type == 'OPEN_P'):
                node = FuncCall(ident)
                Parser.tokens.selectNext()
                if(Parser.tokens.actual.token_type != 'CLOSE_P'):
                    node.children.append(Parser.parseRelEx())
                    while(Parser.tokens.actual.token_type == 'COMMA'):
                        Parser.tokens.selectNext()
                        node.children.append(Parser.parseRelEx())
                if(Parser.tokens.actual.token_type == 'CLOSE_P'):
                    Parser.tokens.selectNext()
                else:
                    raise ValueError(
                        'OPEN_P needs matching CLOSE_P (IDENTIFIER FACTOR)')
            else:
                identifier = Identifier(ident)
                if(Parser.tokens.actual.token_type == 'SET_EQUAL'):
                    Parser.tokens.selectNext()
                    node = Assignement()
                    node.children[0] = identifier
                    if(Parser.tokens.actual.token_type == 'RDLN'):
                        Parser.tokens.selectNext()
                        node.children[1] = ReadLine()
                        if(Parser.tokens.actual.token_type == 'OPEN_P'):
                            Parser.tokens.selectNext()
                            if(Parser.tokens.actual.token_type == 'CLOSE_P'):
                                Parser.tokens.selectNext()
                            else:
                                raise ValueError(
                                    'READLINE: OPEN_P token needs CLOSE_P token after in command')
                        else:
                            raise ValueError(
                                'READLINE token needs OPEN_P token after in command')
                    else:
                        node.children[1] = Parser.parseRelEx()

                else:
                    raise ValueError(
                        "IDENTIFIER (NOT FUNCCALL) token needs SET_EQUAL token after in COMMAND")
        elif(Parser.tokens.actual.token_type == 'PRINT'):
            Parser.tokens.selectNext()
            if(Parser.tokens.actual.token_type == 'OPEN_P'):
                Parser.tokens.selectNext()
                node = Print()
                node.children[0] = Parser.parseRelEx()
                if(Parser.tokens.actual.token_type == 'CLOSE_P'):
                    Parser.tokens.selectNext()
                    return node
                else:
                    raise ValueError('( must have a matching )')
            else:
                raise ValueError('PRINT token needs to be followed by (')
        elif(Parser.tokens.actual.token_type == 'WHILE'):
            Parser.tokens.selectNext()
            node = While()
            node.children[0] = Parser.parseRelEx()
            if(Parser.tokens.actual.token_type == 'END_LINE'):
                Parser.tokens.selectNext()
                node.children[1] = Parser.parseBlock()
                if(Parser.tokens.actual.token_type == 'END'):
                    Parser.tokens.selectNext()
                else:
                    raise ValueError("WHILE needs END token")
            else:
                raise ValueError("WHILE needs END_LINE after RELEX")

        elif(Parser.tokens.actual.token_type == 'IF'):
            Parser.tokens.selectNext()
            node = If()
            node.children[0] = Parser.parseRelEx()
            if(Parser.tokens.actual.token_type == 'END_LINE'):
                Parser.tokens.selectNext()

                node.children[1] = Parser.parseBlock()

                if(Parser.tokens.actual.token_type == 'ELSEIF'):
                    nodes = []
                    while(Parser.tokens.actual.token_type == 'ELSEIF'):
                        Parser.tokens.selectNext()
                        node2 = If()
                        node2.children[0] = Parser.parseRelEx()
                        if(Parser.tokens.actual.token_type == 'END_LINE'):
                            Parser.tokens.selectNext()
                            node2.children[1] = Parser.parseBlock()
                            nodes.append(node2)
                        else:
                            raise ValueError("ELSEIF needs END_LINE after")

                    node.children[2] = nodes[0]
                    for i in range(len(nodes)):
                        if(i != len(nodes) - 1):
                            nodes[i].children[2] = nodes[i+1]

                    if(Parser.tokens.actual.token_type == 'ELSE'):
                        Parser.tokens.selectNext()
                        if(Parser.tokens.actual.token_type == 'END_LINE'):
                            Parser.tokens.selectNext()
                            node2 = Else()
                            node2.children[0] = Parser.parseBlock()
                            nodes[-1].children[2] = node2
                            if(Parser.tokens.actual.token_type == 'END'):
                                Parser.tokens.selectNext()
                            else:
                                raise ValueError("ELSE needs END token")
                        else:
                            raise ValueError("ELSE needs END_LINE after")
                    elif(Parser.tokens.actual.token_type == 'END'):
                        Parser.tokens.selectNext()
                    else:
                        raise ValueError("IF needs END token")

                elif(Parser.tokens.actual.token_type == 'ELSE'):
                    Parser.tokens.selectNext()
                    if(Parser.tokens.actual.token_type == 'END_LINE'):
                        Parser.tokens.selectNext()
                        node2 = Else()
                        node2.children[0] = Parser.parseBlock()
                        node.children[2] = node2
                        if(Parser.tokens.actual.token_type == 'END'):
                            Parser.tokens.selectNext()
                        else:
                            raise ValueError("ELSE needs END token")
                    else:
                        raise ValueError("ELSE needs END_LINE after")
                elif(Parser.tokens.actual.token_type == 'END'):
                    Parser.tokens.selectNext()
                else:
                    raise ValueError("IF needs END token")
            else:
                raise ValueError("IF needs END_LINE after RELEX")

        elif(Parser.tokens.actual.token_type == 'LOCAL'):
            Parser.tokens.selectNext()
            if(Parser.tokens.actual.token_type == 'IDENTIFIER'):
                node = TypeAssignement()
                node.children[0] = Identifier(Parser.tokens.actual.token_value)
                Parser.tokens.selectNext()
                if(Parser.tokens.actual.token_type == 'SET_TYPE'):
                    Parser.tokens.selectNext()
                    if(Parser.tokens.actual.token_type == 'INT_TYPE' or Parser.tokens.actual.token_type == 'BOOL_TYPE' or Parser.tokens.actual.token_type == 'STRING_TYPE'):
                        node.children[1] = Parser.tokens.actual.token_value
                        Parser.tokens.selectNext()
                    else:
                        raise ValueError("Needs TYPE after SET_TYPE")
                else:
                    raise ValueError(
                        "Needs SET_TYPE after IDENTIFIER after LOCAL")
            else:
                raise ValueError("Needs IDENTIFIER after LOCAL")
        elif(Parser.tokens.actual.token_type == 'RETURN'):
            node = Return()
            Parser.tokens.selectNext()
            node.children[0] = Parser.parseRelEx()

        if(Parser.tokens.actual.token_type == 'END_LINE'):
            Parser.tokens.selectNext()
            return node
        else:
            raise ValueError("Needs END_LINE token")

    @staticmethod
    def parseRelEx():
        result = Parser.parseExpression()
        while(Parser.tokens.actual.token_type == 'EQUALS' or Parser.tokens.actual.token_type == 'GREATER' or Parser.tokens.actual.token_type == 'SMALLER'):
            if Parser.tokens.actual.token_type == 'EQUALS' or Parser.tokens.actual.token_type == 'GREATER' or Parser.tokens.actual.token_type == 'SMALLER':
                node = BinOp(Parser.tokens.actual.token_value)
                node.children[0] = result
                result = node
                Parser.tokens.selectNext()
                result.children[1] = Parser.parseExpression()
        return result

    @staticmethod
    def parseBlock():
        main_node = Statement()
        while(Parser.tokens.actual.token_type != 'EOF' and Parser.tokens.actual.token_type != 'END' and Parser.tokens.actual.token_type != 'ELSE' and Parser.tokens.actual.token_type != 'ELSEIF'):
            main_node.children.append(Parser.parseCommand())
        return main_node

    @staticmethod
    def parseBlockMain():
        main_node = Statement()
        while(Parser.tokens.actual.token_type != 'EOF'):
            if(Parser.tokens.actual.token_type == 'FUNCTION'):
                Parser.tokens.selectNext()
                if(Parser.tokens.actual.token_type == 'IDENTIFIER'):
                    func_node = FuncDec(Parser.tokens.actual.token_value, None)
                    main_node.children.append(func_node)
                    Parser.tokens.selectNext()
                    if(Parser.tokens.actual.token_type == 'OPEN_P'):
                        Parser.tokens.selectNext()
                        if(Parser.tokens.actual.token_type == 'IDENTIFIER'):
                            ident_node = [None, None]
                            ident_node[0] = Parser.tokens.actual.token_value
                            Parser.tokens.selectNext()
                            if(Parser.tokens.actual.token_type == 'SET_TYPE'):
                                Parser.tokens.selectNext()
                                if(Parser.tokens.actual.token_type == 'INT_TYPE' or Parser.tokens.actual.token_type == 'BOOL_TYPE' or Parser.tokens.actual.token_type == 'STRING_TYPE'):
                                    ident_node[1] = Parser.tokens.actual.token_value
                                    func_node.children.append(ident_node)
                                    Parser.tokens.selectNext()
                                    while(Parser.tokens.actual.token_type == 'COMMA'):
                                        Parser.tokens.selectNext()
                                        if(Parser.tokens.actual.token_type == 'IDENTIFIER'):
                                            ident_node = [None, None]
                                            ident_node[0] = Parser.tokens.actual.token_value
                                            Parser.tokens.selectNext()
                                            if(Parser.tokens.actual.token_type == 'SET_TYPE'):
                                                Parser.tokens.selectNext()
                                                if(Parser.tokens.actual.token_type == 'INT_TYPE' or Parser.tokens.actual.token_type == 'BOOL_TYPE' or Parser.tokens.actual.token_type == 'STRING_TYPE'):
                                                    ident_node[1] = Parser.tokens.actual.token_value
                                                    func_node.children.append(
                                                        ident_node)
                                                    Parser.tokens.selectNext()
                                                else:
                                                    raise ValueError(
                                                        'FUNCTION SET_TYPE needs TYPE after')
                                            else:
                                                raise ValueError(
                                                    'FUNCTION IDENTIFIER needs SET_TYPE after')
                                        else:
                                            raise ValueError(
                                                'FUNCTION needs IDENTIFIER after COMMA')
                                else:
                                    raise ValueError(
                                        'FUNCTION SET_TYPE needs TYPE after')
                            else:
                                raise ValueError(
                                    'FUNCTION IDENTIFIER needs SET_TYPE after')
                        if(Parser.tokens.actual.token_type == 'CLOSE_P'):
                            Parser.tokens.selectNext()
                            if(Parser.tokens.actual.token_type == 'SET_TYPE'):
                                Parser.tokens.selectNext()
                                if(Parser.tokens.actual.token_type == 'INT_TYPE' or Parser.tokens.actual.token_type == 'BOOL_TYPE' or Parser.tokens.actual.token_type == 'STRING_TYPE'):
                                    func_node._type = Parser.tokens.actual.token_value
                                    Parser.tokens.selectNext()
                                    if(Parser.tokens.actual.token_type == 'END_LINE'):
                                        Parser.tokens.selectNext()
                                        statement_node = Parser.parseBlock()
                                        func_node.children.append(
                                            statement_node)
                                        if(Parser.tokens.actual.token_type == 'END'):
                                            Parser.tokens.selectNext()
                                            if(Parser.tokens.actual.token_type == 'END_LINE'):
                                                Parser.tokens.selectNext()
                                            else:
                                                raise ValueError(
                                                    'END needs END_LINE after')
                                        else:
                                            raise ValueError(
                                                'FUNCTION needs END')
                                    else:
                                        raise ValueError(
                                            'FUNCTION needs END_LINE after TYPE')
                                else:
                                    raise ValueError(
                                        'FUNCTION SET_TYPE needs TYPE after')
                            else:
                                raise ValueError(
                                    'FUNCTION CLOSE_P needs SET_TYPE after')
                        else:
                            raise ValueError(
                                'FUNCTION OPEN_P needs matching CLOSE_P')
                    else:
                        raise ValueError(
                            'FUNCTION IDENTIFIER needs OPEN_P after')
                else:
                    raise ValueError('FUNCTION needs IDENTIFIER after')
            else:
                main_node.children.append(Parser.parseCommand())
        return main_node

    @staticmethod
    def run(code):
        Parser.tokens = Tokenizer(code)
        result = Parser.parseBlockMain()
        if(Parser.tokens.actual.token_type == 'EOF'):
            return result
        else:
            raise ValueError('Ended Before EOF')
