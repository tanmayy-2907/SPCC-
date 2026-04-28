%{
#include <stdio.h>
%}

%%
[0-9]+"."[0-9]+    { printf("Floating-point Number: %s\n", yytext); }
[0-9]+             { printf("Integer: %s\n", yytext); }
[ \t\n]            { /* Skip whitespace */ }
.                  { printf("Invalid Character: %s\n", yytext); }
%%

int main() {
    printf("Enter numbers to classify (Ctrl+D to exit):\n");
    yylex();
    return 0;
}

int yywrap() {
    return 1;
}