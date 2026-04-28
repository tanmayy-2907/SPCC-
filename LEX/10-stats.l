%{
#include <stdio.h>
int d=0, a=0, s=0;
%}

%%
[0-9]       { d++; }
[a-zA-Z]    { a++; }
[ \t]       { /* Ignore whitespace */ }
\n	    { return 0; }
.           { s++; }
%%

int yywrap() { return 1; }

int main() {
    printf("Enter input:\n");
    yylex();
    printf("Alphabets: %d\nDigits: %d\nSpecial Symbols: %d\n", a, d, s);
    return 0;
}