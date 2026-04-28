%{
#include <stdio.h>
#include <string.h>
void check_palindrome(char*);
%}

%%
[a-zA-Z0-9]+    { check_palindrome(yytext); }
\n              {  }
.               { /* Skip */ }
%%

void check_palindrome(char *str) {
    int i = 0;
    int j = strlen(str) - 1;
    while (j > i) {
        if (str[i++] != str[j--]) {
            printf("%s is NOT a palindrome.\n", str);
            return;
        }
    }
    printf("%s is a palindrome.\n", str);
}

int yywrap() { return 1; }

int main() {
    printf("Enter a string: ");
    yylex();
    return 0;
}