%{
#include <stdio.h>
%}

%%
[0-9]+		{ printf("Number: %s\n", yytext); }
[a-zA-Z]+	{ printf("Word: %s\n", yytext); }
[ \t\n]+	{ /* Ignore whitespace */ }
.		{ printf("Invalid input: %s\n", yytext); }
%%

int yywrap() {
    return 1;
}

int main() {
    printf("Enter a string: ");
    yylex();
    return 0;
}
