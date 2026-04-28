%{
#include <stdio.h>
%}

%%
[0-9]       { printf("%s is a Digit\n", yytext); }
[a-zA-Z]    { printf("%s is an Alphabet\n", yytext); }
\n          { /* Skip */ }
.           { printf("%s is a Special Symbol\n", yytext); }
%%

int yywrap() { return 1; }

int main() {
    printf("Enter a character: ");
    yylex();
    return 0;
}