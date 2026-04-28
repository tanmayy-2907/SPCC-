%{
#include <stdio.h>
int opec = 0, opac = 0; 
%}

%%
"+"|"-"|"*"|"/"|"="|"==" { opec++; }
[a-zA-Z_][a-zA-Z0-9_]* 		{ opac++; }
[0-9]+				{ opac++; }
[ \t\n]+			{  }
.				{  }
%%

int yywrap() { return 1; }

int main() {
    printf("Enter an expression: ");
    yylex();
    printf("\nTotal Operators: %d\nTotal Operands: %d\n", opec, opac);
    return 0;
}