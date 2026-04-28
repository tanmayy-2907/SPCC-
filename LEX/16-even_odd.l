%{
#include <stdio.h>
#include <stdlib.h>
int num;
%}

%%
[0-9]+ {
    num = atoi(yytext);
    if (num % 2 == 0)
        printf("%d is EVEN\n", num);
    else
        printf("%d is ODD\n", num);
}
\n     {  }
.      { /* Skip */ }
%%

int yywrap() { return 1; }

int main() {
    printf("Enter a number: ");
    yylex();
    return 0;
}