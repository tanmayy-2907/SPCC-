%{
#include <stdio.h>
%}

%%
int|float|char|double|if|else|for|while|do|return|void|switch|case|break {
    printf("Invalid (keyword): %s\n", yytext);
}
^[a-zA-Z_][a-zA-Z0-9_]*	{ printf("Valid identifier: %s\n", yytext); }
.*			{ printf("Invalid identifier: %s\n", yytext); }
\n			{  }
%%

int yywrap() { return 1; }

int main() {
    printf("Enter a string to check if it's a valid C identifier: ");
    yylex();
    return 0;
}