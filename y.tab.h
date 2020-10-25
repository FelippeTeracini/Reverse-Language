/* A Bison parser, made by GNU Bison 3.0.4.  */

/* Bison interface for Yacc-like parsers in C

   Copyright (C) 1984, 1989-1990, 2000-2015 Free Software Foundation, Inc.

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

#ifndef YY_YY_Y_TAB_H_INCLUDED
# define YY_YY_Y_TAB_H_INCLUDED
/* Debug traces.  */
#ifndef YYDEBUG
# define YYDEBUG 0
#endif
#if YYDEBUG
extern int yydebug;
#endif

/* Token type.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
  enum yytokentype
  {
    QUOTES = 258,
    DEFINE = 259,
    SEMI_COLUMN = 260,
    COMMA = 261,
    OPEN_P = 262,
    CLOSE_P = 263,
    OPEN_B = 264,
    CLOSE_B = 265,
    DEF = 266,
    RETURN = 267,
    INPUT = 268,
    WHILE = 269,
    IF = 270,
    ELIF = 271,
    ELSE = 272,
    AND = 273,
    OR = 274,
    PRINT = 275,
    TRUE = 276,
    FALSE = 277,
    EQUALS = 278,
    NOT = 279,
    LESS = 280,
    MORE = 281,
    LESS_E = 282,
    MORE_E = 283,
    PLUS = 284,
    MINUS = 285,
    MULT = 286,
    DIV = 287,
    REST = 288,
    DIV_INT = 289,
    POW = 290,
    DATA_TYPE = 291,
    CHARACTER_VALUE = 292,
    INTEGER_VALUE = 293,
    FLOAT_VALUE = 294,
    STRING_VALUE = 295,
    IDENTIFIER_VALUE = 296
  };
#endif
/* Tokens.  */
#define QUOTES 258
#define DEFINE 259
#define SEMI_COLUMN 260
#define COMMA 261
#define OPEN_P 262
#define CLOSE_P 263
#define OPEN_B 264
#define CLOSE_B 265
#define DEF 266
#define RETURN 267
#define INPUT 268
#define WHILE 269
#define IF 270
#define ELIF 271
#define ELSE 272
#define AND 273
#define OR 274
#define PRINT 275
#define TRUE 276
#define FALSE 277
#define EQUALS 278
#define NOT 279
#define LESS 280
#define MORE 281
#define LESS_E 282
#define MORE_E 283
#define PLUS 284
#define MINUS 285
#define MULT 286
#define DIV 287
#define REST 288
#define DIV_INT 289
#define POW 290
#define DATA_TYPE 291
#define CHARACTER_VALUE 292
#define INTEGER_VALUE 293
#define FLOAT_VALUE 294
#define STRING_VALUE 295
#define IDENTIFIER_VALUE 296

/* Value type.  */
#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED

union YYSTYPE
{
#line 12 "syntax.y" /* yacc.c:1909  */

	char* dataType;
	char charVal;
	int intVal;
	float floatVal;
	char* strVal;

#line 144 "y.tab.h" /* yacc.c:1909  */
};

typedef union YYSTYPE YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define YYSTYPE_IS_DECLARED 1
#endif


extern YYSTYPE yylval;

int yyparse (void);

#endif /* !YY_YY_Y_TAB_H_INCLUDED  */
