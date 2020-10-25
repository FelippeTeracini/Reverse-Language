/* https://github.com/ajhalthor/interpreter */
%{
    #include <string.h>
    #include <stdlib.h>
    #include "y.tab.h"
    void extern yyerror(char*);
    void InvalidToken();
%}

whitespace      [ \t\r\v\f]
linefeed        \n

%%
""\"											{return QUOTES;}
"="												{return DEFINE;}
";"												{return	SEMI_COLUMN;}
","												{return	COMMA;}
")"												{return OPEN_P;}
"("												{return CLOSE_P;}
"}"												{return OPEN_B;}
"{"												{return CLOSE_B;}
"fed"											{return DEF;}
"nruter"                                        {return RETURN;}
"tupni"                                         {return INPUT;}
"elihw"											{return WHILE;}
"fi"											{return IF;}
"file"											{return ELIF;}
"esle"											{return ELSE;}
"dna"											{return AND;}
"ro"											{return OR;}
"tnirp"                                         {return PRINT;}
"eurt"                                          {return TRUE;}
"eslaf"                                         {return FALSE;}
"=="											{return EQUALS;}
"!"											    {return NOT;}
">"											    {return LESS;}
"<"											    {return MORE;}
"=>"											{return LESS_E;}
"=<"											{return MORE_E;}
"+"												{return	PLUS;}
"-"												{return MINUS;}
"*"												{return MULT;}
"\\"											{return DIV;}
"%"												{return REST;}
"\\\\"											{return DIV_INT;}
"^"											    {return POW;}
[\"][a-zA-Z][\"]								{yylval.charVal = yytext[1]; return CHARACTER_VALUE;}
[0-9]+                                          {yylval.intVal = atoi(yytext); return INTEGER_VALUE;}
[0-9]*\.?[0-9]+                                 {yylval.floatVal = atof(yytext); return FLOAT_VALUE;}
[a-zA-Z][_a-zA-Z0-9]*							{yylval.strVal = strdup(yytext); return IDENTIFIER_VALUE;}
\"(\\.|[^"])*\"                                 {yylval.strVal = strdup(yytext); return STRING_VALUE;}


{linefeed}                                      {yylineno++;}
{whitespace}                                    ;
.                                               {InvalidToken();}
%%

int yywrap(void){
    return 1;
}

void yyerror(char *s) {
    fprintf(stderr, "\nERROR ON LINE %d : \n %s\n", yylineno, s);
    exit(0);
}

void InvalidToken(){
    printf("ERROR ON LINE %d : \n Invalid Token %s\n", yylineno,yytext);
    exit(0);
}
