%{
#include<stdio.h>
int vow=0;
int const_count=0;
%}

%%
[aeiouAEIOU] {vow++;}
[a-zA-Z] {const_count++;}
%%
int yywrap(){
    return 1;
}
int main(){
    printf("Enter the string: ");
    yylex();
    printf("no. of vowels are: %d\n",vow);
    printf("no. of consonants are %d",const_count);
    return 0;
}
