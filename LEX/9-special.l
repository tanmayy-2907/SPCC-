%{
#include <stdio.h>
%}

%%
[a-zA-Z0-9]    { /* Ignore letters and digits */ }
[ \t\n]        { /* Ignore whitespace */ }
.              { printf("Special Character Found: %s\n", yytext); }
%%

int yywrap() { return 1; }

int main() {
    printf("Enter string to find special characters: ");
    yylex();
    return 0;
}