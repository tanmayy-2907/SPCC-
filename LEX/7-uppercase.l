%{
#include <stdio.h>
#include <ctype.h>
%}

%%
[a-z]		{ printf("%c", yytext[0]-32); }
.		{ printf("%s", yytext); }
\n		{ }
%%

int yywrap() { return 1; }

int main() {
    printf("Enter text in lowercase:\n");
    yylex();
    return 0;
} 