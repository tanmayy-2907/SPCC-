%{
#include <stdio.h>
int v_count = 0;
%}

%%
[aeiouAEIOU]    { v_count++; }
[a-zA-Z]        { /* Consonants - ignore */ }
\n              { return 0; } /* End on Enter */
.               { /* Ignore others */ }
%%

int yywrap() { return 1; }

int main() {
    printf("Enter a string: ");
    yylex();
    printf("Total Vowels: %d\n", v_count);
    return 0;
}