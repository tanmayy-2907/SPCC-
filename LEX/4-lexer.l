%{
#include <stdio.h>
%}

/* Definitions for common patterns */
digit       [0-9]
letter      [a-zA-Z]
id          {letter}({letter}|{digit})*
num         {digit}+(\.{digit}+)?

%%
"int"|"float"|"char"|"if"|"else"|"while"|"return"|"main" {
    printf("Keyword: %s\n", yytext);
}

{id} {
    printf("Identifier: %s\n", yytext);
}

{num} {
    printf("Number: %s\n", yytext);
}

"+"|"-"|"*"|"/"|"="|"==" {
    printf("Operator: %s\n", yytext);
}

"("|")"|"{"|"}"|","|";" {
    printf("Punctuation: %s\n", yytext);
}

[ \t\n]+ { /* Skip whitespace */ }

. {
    printf("Unknown Character: %s\n", yytext);
}
%%

int yywrap() {
    return 1;
}

int main() {
    printf("Enter code snippet to analyze:\n");
    yylex();
    return 0;
}