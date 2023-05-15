%{
    #include<stdio.h>
%}
lower [a-z]
%%
{lower} printf("%c",yytext[0]-32);
%%
int main(){
yylex();
}
int yywrap(){
return 1;
}