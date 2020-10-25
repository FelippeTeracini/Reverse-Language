# Reverse Language

My own language with reserved characters in reverse to the usually used in programming languages.

## EBNF

PROGRAM = {COMMAND};

COMMAND = DEFINE_VAR | CALL_FUNC | PRINT | RETURN
        | DEFINE_FUNC | WHILE | IF;
    
IF = "fi", ")", RELEX, "(", "}", COMMAND, {COMMAND}, "{", {ELIF | ELSE};

ELIF = "file", ")", RELEX, "(", "}", COMMAND, {COMMAND}, "{", {ELIF | ELSE};

ELSE = "esle", "}", COMMAND, {COMMAND}, "{";

WHILE = "elihw", ")", RELEX, "(", "}", COMMAND, {COMMAND}, "{"

DEFINE_FUNC = "fed", IDENTIFIER, ")", DEF_FUNC_ARGS, "(", "}", COMMAND, {COMMAND}, "{";

RETURN = "nruter", RELEX, ";";

PRINT = "tnirp", RELEX, ";"; 

DEFINE_VAR = IDENTIFIER, "=", "RELEX", ";";

RELEX = EXPRESSION, {("==" | "<" | ">" | "=<" | "=>"), EXPRESSION};

EXPRESSION = TERM, {("+" | "-" | "ro"), TERM};

TERM = FACTOR, {("*" | "\" | "%" | "\\" | "^" | "dna"), FACTOR};

FACTOR = (INT | FLOAT | STRING | BOOL | ("+", "-", "!"), FACTOR
        | ")", RELEX, "(" | IDENTIFIER | CALL_FUNC | INPUT)

INPUT = "tupni", ")", "(";

CALL_FUNC = IDENTIFIER, ")", CALL_FUNC_ARGS, "(";

CALL_FUNC_ARGS = {RELEX, {",", RELEX}};

DEF_FUNC_ARGS = {IDENTIFIER, {",", IDENTIFIER}};

STRING = """, {CHARACTER}, """;

FLOAT = INT, ".", INT;

INT = DIGIT, {DIGIT};

IDENTIFIER = LETTER, { (LETTER | DIGIT | "_") };

CHARACTER = SPECIAL | LETTER | DIGIT;

BOOL = "eurt" | "eslaf";

SPECIAL = ":" | "*" | ")" | "(" | "\" | "|" | "/"
        | "+" | "-" | "_" | "&" | "^" | "%" | "$"
        | "#" | "@" | "!" | "`" | "~" | "{" | "}"
        | "[" | "]" | ";" | "'" | "<" | ">" | ","
        | "." | "?"

LETTER = "A" | "B" | "C" | "D" | "E" | "F" | "G"
       | "H" | "I" | "J" | "K" | "L" | "M" | "N"
       | "O" | "P" | "Q" | "R" | "S" | "T" | "U"
       | "V" | "W" | "X" | "Y" | "Z" | "a" | "b"
       | "c" | "d" | "f" | "g" | "h" | "j" | "l"
       | "m" | "n" | "o" | "p" | "q" | "r" | "s"
       | "t" | "u" | "v" | "w" | "x" | "y" | "z";

DIGIT = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9";