%{
#include <stdio.h>
%}

%%
[aeiouAEIOU]	{ printf("%s is a Vowel\n", yytext); }
[a-zA-Z]        { printf("%s is a Consonant\n", yytext); }
[0-9]           { printf("%s is a Digit (Not a letter)\n", yytext); }
\n              { /* Ignore newline */ }
.               { printf("%s is a Special Character\n", yytext); }
%%

int yywrap() {
    return 1;
}

int main() {
    printf("Enter a character: ");
    yylex();
    return 0;
}
