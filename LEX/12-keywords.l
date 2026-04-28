%{
#include <stdio.h>
%}

%%
int|float|char|double|if|else|for|while|do|return|void|switch|case|break {
    printf("Keyword: %s\n", yytext);
}
[a-zA-Z_][a-zA-Z0-9_]* {
    printf("Not a keyword (Regular Identifier): %s\n", yytext);
}
.|\n { /* Ignore everything else */ }
%%

int yywrap() { return 1; }

int main() {
    printf("Enter text to extract keywords: ");
    yylex();
    return 0;
}