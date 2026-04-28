%{
#include <stdio.h>
int sc=0, tc=0; 
%}

%%
" "	{ sc++; }
\t	{ tc++; }
\n	{ return 0; }
.	{ }
%%

int yywrap() { return 1; }

int main() {
    printf("Enter a string with spaces and tabs: ");
    yylex();
    printf("Spaces: %d\nTabs: %d\n", sc, tc);
    return 0;
}