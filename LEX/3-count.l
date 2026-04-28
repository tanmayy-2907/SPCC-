%{
#include <stdio.h>
int lines=0, words=0, chars=0; 
%}

%%
\n		{ lines++; chars++; }
[ \t]		{ chars++; }
[^\t\n ]+	{ words++; chars += yyleng; }
%%

int yywrap()
{
    return 1; 
}  

int main()
{
    printf("Enter text:\n");
    yylex();
    printf("\nLines: %d\nWords: %d\nCharacters: %d\n", lines, words, chars);
    return 0;
}

